# Performance Optimization

Profile before optimizing. Use [React DevTools](https://react.dev/learn/react-developer-tools) or [React Scan](https://react-scan.com/) to confirm a re-render problem actually exists before reaching for these techniques.

## React.memo

```tsx
import { memo } from 'react';

const ExpensiveList = memo(function ExpensiveList({ items }: { items: Item[] }) {
  return <ul>{items.map(item => <li key={item.id}>{item.name}</li>)}</ul>;
});

// Custom comparison when shallow prop equality isn't enough
const UserCard = memo(
  function UserCard({ user }: { user: User }) {
    return <div>{user.name}</div>;
  },
  (prevProps, nextProps) => prevProps.user.id === nextProps.user.id
);
```

## Preventing Unnecessary Re-renders

```tsx
// ❌ New object/function created every render, defeats memo() on Child
function Parent() {
  return <Child style={{ color: 'red' }} onClick={() => doSomething()} />;
}

// ✅ Stable references
const style = { color: 'red' };
function Parent() {
  const handleClick = useCallback(() => doSomething(), []);
  return <Child style={style} onClick={handleClick} />;
}
```

## Code Splitting with lazy()

```tsx
import { lazy, Suspense } from 'react';

const HeavyChart = lazy(() => import('./HeavyChart'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      {showChart && <HeavyChart data={data} />}
    </Suspense>
  );
}
```

## Virtualization (large lists — 1000+ items)

```tsx
import { useVirtualizer } from '@tanstack/react-virtual';

function VirtualList({ items }: { items: Item[] }) {
  const parentRef = useRef<HTMLDivElement>(null);
  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
  });

  return (
    <div ref={parentRef} style={{ height: '400px', overflow: 'auto' }}>
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map((v) => (
          <div key={v.key} style={{ position: 'absolute', top: v.start, height: v.size }}>
            {items[v.index].name}
          </div>
        ))}
      </div>
    </div>
  );
}
```

## useMemo for Expensive Calculations

```tsx
function Analytics({ data }: { data: DataPoint[] }) {
  const stats = useMemo(() => ({
    total: data.reduce((sum, d) => sum + d.value, 0),
    average: data.reduce((sum, d) => sum + d.value, 0) / data.length,
    max: Math.max(...data.map(d => d.value)),
  }), [data]);

  return <StatsDisplay stats={stats} />;
}
```

## useTransition for Non-urgent Updates

```tsx
import { useTransition } from 'react';

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<Item[]>([]);
  const [isPending, startTransition] = useTransition();

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    setQuery(e.target.value); // urgent
    startTransition(() => {
      setResults(filterItems(e.target.value)); // interruptible
    });
  }

  return (
    <>
      <input value={query} onChange={handleChange} />
      {isPending ? <Spinner /> : <Results items={results} />}
    </>
  );
}
```

## Quick Reference

| Technique | When to Use |
|-----------|-------------|
| `memo()` | Prevent re-renders from unchanged props |
| `useMemo()` | Cache expensive calculations |
| `useCallback()` | Stable function references for memoized children |
| `lazy()` | Code split heavy components |
| `useTransition()` | Keep UI responsive during non-urgent updates |
| Virtualization | Large lists (1000+ items) |

| Anti-pattern | Fix |
|--------------|-----|
| Inline objects passed to memoized children | Lift out or `useMemo` |
| Inline functions passed to memoized children | `useCallback` |
| Large bundle | `lazy()` + `Suspense` |
| Long lists | Virtualization |
| Memoizing everything by default | Measure first; only memoize what's actually expensive |
