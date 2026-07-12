# Hooks & State Management

## Choosing a State Approach

| Solution | Best For |
|----------|----------|
| `useState` | Local component state |
| Context | Theme, auth flags, simple low-frequency globals |
| Zustand | Medium-complexity client state, minimal boilerplate |
| Redux Toolkit | Complex client state, middleware, devtools, team-wide conventions |
| TanStack Query | Server state — data fetched from an API, caching, invalidation |

Default to the simplest option that fits. Don't introduce Redux Toolkit for state a `useState`/Context could handle; don't hand-roll fetch/cache logic that TanStack Query already solves well.

## Local State

```tsx
function Counter() {
  const [count, setCount] = useState(0);
  const increment = () => setCount(prev => prev + 1); // functional update
  return <button onClick={increment}>{count}</button>;
}
```

## Context for Simple Global State

```tsx
interface ThemeContextValue {
  theme: 'light' | 'dark';
  toggle: () => void;
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');
  const toggle = useCallback(() => {
    setTheme(t => (t === 'light' ? 'dark' : 'light'));
  }, []);
  // Memoize the value so consumers don't re-render on every provider render
  const value = useMemo(() => ({ theme, toggle }), [theme, toggle]);

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) throw new Error('useTheme must be used within ThemeProvider');
  return context;
}
```

## Redux Toolkit

```tsx
import { createSlice, configureStore, PayloadAction } from '@reduxjs/toolkit';
import { Provider, useSelector, useDispatch } from 'react-redux';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1 },
    incrementBy: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    },
  },
});

const store = configureStore({ reducer: { counter: counterSlice.reducer } });

type RootState = ReturnType<typeof store.getState>;
type AppDispatch = typeof store.dispatch;

const useAppSelector = useSelector.withTypes<RootState>();
const useAppDispatch = useDispatch.withTypes<AppDispatch>();

function Counter() {
  const count = useAppSelector((state) => state.counter.value);
  const dispatch = useAppDispatch();
  return (
    <button onClick={() => dispatch(counterSlice.actions.increment())}>
      {count}
    </button>
  );
}
```

Keep slices scoped to a single domain. Use `createSelector` (Reselect, bundled with RTK) for derived state to avoid recomputation on every render.

## TanStack Query (Server State)

Use for anything fetched from a server — don't model server data as component/Redux state managed by hand.

```tsx
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function UserProfile({ userId }: { userId: string }) {
  const queryClient = useQueryClient();

  const { data, isLoading, error } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
    staleTime: 5 * 60 * 1000,
  });

  const mutation = useMutation({
    mutationFn: updateUser,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['user', userId] });
    },
  });

  if (isLoading) return <Skeleton />;
  if (error) return <ErrorState error={error} />;

  return <UserCard user={data} onUpdate={mutation.mutate} />;
}
```

Query keys should be structured (`['user', userId]`, not a flat string) so targeted invalidation works. Don't duplicate server data into Redux/Context — TanStack Query's cache is the source of truth for it.

## Zustand (lightweight alternative to Redux Toolkit)

```tsx
import { create } from 'zustand';

interface CartStore {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  clear: () => void;
}

const useCartStore = create<CartStore>((set) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
  clear: () => set({ items: [] }),
}));
```

Reach for this instead of Redux Toolkit when the team doesn't need middleware/devtools conventions and wants less boilerplate.

## Custom Hook Patterns

### Data Fetching (when not using TanStack Query)

```tsx
function useApi<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const controller = new AbortController();
    fetch(url, { signal: controller.signal })
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(setData)
      .catch(err => { if (err.name !== 'AbortError') setError(err); })
      .finally(() => setLoading(false));
    return () => controller.abort();
  }, [url]);

  return { data, error, loading };
}
```

### useDebounce

```tsx
function useDebounce<T>(value: T, delay: number): T {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);
  return debounced;
}
```

### useLocalStorage

```tsx
function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    if (typeof window === 'undefined') return initialValue;
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initialValue;
  });
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);
  return [value, setValue] as const;
}
```

### useMediaQuery

```tsx
function useMediaQuery(query: string): boolean {
  const [matches, setMatches] = useState(() =>
    typeof window !== 'undefined' && window.matchMedia(query).matches
  );
  useEffect(() => {
    const media = window.matchMedia(query);
    const listener = (e: MediaQueryListEvent) => setMatches(e.matches);
    media.addEventListener('change', listener);
    return () => media.removeEventListener('change', listener);
  }, [query]);
  return matches;
}
```

## Effect Rules

- Always clean up subscriptions, timers, and listeners.
- Use a `cancelled`/`AbortController` guard in async effects so state isn't set after unmount or after a newer request has superseded an older one.
- Dependency arrays must include everything the effect closes over. Missing deps cause stale-closure bugs; use functional updates (`setCount(prev => prev + 1)`) to sidestep needing the value itself as a dependency.

```tsx
useEffect(() => {
  let cancelled = false;
  async function run() {
    const data = await api.getData();
    if (!cancelled) setData(data);
  }
  run();
  return () => { cancelled = true };
}, [/* deps */]);
```

### Don't guess at layout timing with chained rAF / setTimeout

Nesting `requestAnimationFrame` (or piling on `setTimeout`) to "wait until the DOM
has settled" is a magic-number timing hack, not a synchronization mechanism. It
happens to work on the author's machine and silently breaks under different render
timing — slower devices, more rows, a heavier commit. There's no signal that says
"measurement is done" here; the frame count is a guess.

```tsx
// ❌ Anti-pattern: triple rAF to "ensure the virtualizer has measured"
requestAnimationFrame(() => {
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      if (scrollRef.current) {
        scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
      }
    });
  });
});
```

Subscribe to the actual "layout changed" signal instead:

- **`useLayoutEffect`** keyed to the measured value, so the scroll runs synchronously
  after the DOM reflects that value and before paint.
- **`ResizeObserver`** when you need to react to an element's measured size settling.
- **A virtualizer's own measurement API** — e.g. TanStack Virtual exposes total size
  and remeasure callbacks; scroll in response to those, not to a frame guess.

```tsx
// ✅ Scroll when the measured size actually changes
useLayoutEffect(() => {
  const el = scrollRef.current;
  if (el) el.scrollTop = el.scrollHeight;
}, [totalSize]); // totalSize from the virtualizer / observed height
```

If you genuinely need to defer past one paint, a *single* `requestAnimationFrame` with
a comment explaining why is the ceiling — chaining more is a smell that you're guessing.

## useCallback & useMemo

```tsx
// useCallback: stable reference for a child that's wrapped in memo()
const handleClick = useCallback((id: string) => setSelected(id), []);

// useMemo: cache a genuinely expensive calculation
const sortedItems = useMemo(
  () => [...items].sort((a, b) => a.name.localeCompare(b.name)),
  [items]
);
```

Don't wrap every function in `useCallback` or every value in `useMemo` — only when passed to a memoized child or the computation is measurably expensive. Over-memoization adds cognitive overhead and comparison cost for no benefit.

## React 19 Additions

### `use()` — read a promise or context in render

```tsx
function Comments({ commentsPromise }: { commentsPromise: Promise<Comment[]> }) {
  const comments = use(commentsPromise); // suspends until resolved
  return <ul>{comments.map(c => <li key={c.id}>{c.text}</li>)}</ul>;
}
```

Unlike other hooks, `use()` can be called conditionally — but only inside a Component or Hook.

### `useActionState` — form state + pending, in one hook

```tsx
'use client';
function NewsletterForm() {
  const [state, formAction, isPending] = useActionState(submitAction, {});
  return (
    <form action={formAction}>
      <input name="email" type="email" required disabled={isPending} />
      <button type="submit" disabled={isPending}>
        {isPending ? 'Subscribing…' : 'Subscribe'}
      </button>
      {state.error && <p>{state.error}</p>}
    </form>
  );
}
```

### `useOptimistic` — optimistic UI updates

```tsx
function TodoList({ todos }: { todos: Todo[] }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo: Todo) => [...state, newTodo]
  );
  async function addTodo(formData: FormData) {
    addOptimisticTodo({ id: 'temp', text: formData.get('text') as string, completed: false });
    await createTodo(formData);
  }
  // ...
}
```

### `ref` as a prop — no `forwardRef` needed

```tsx
function Input({ ref, ...props }: { ref?: React.Ref<HTMLInputElement> } & JSX.IntrinsicElements['input']) {
  return <input ref={ref} {...props} />;
}
```

## Quick Reference

| Hook | Purpose |
|------|---------|
| `useState` | Component state |
| `useEffect` | Side effects, subscriptions |
| `useCallback` | Memoize functions |
| `useMemo` | Memoize values |
| `useRef` | Mutable ref, DOM access |
| `useContext` | Read context |
| `useReducer` | Complex local state logic |
| `use()` | Read promise/context (React 19) |
| `useActionState` | Form action + pending state (React 19) |
| `useOptimistic` | Optimistic UI updates (React 19) |
