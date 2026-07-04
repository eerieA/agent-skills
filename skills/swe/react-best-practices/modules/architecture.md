# Architecture & File Structure

Generalized from a component-generation pipeline's architectural rules — these apply regardless of how the component originated (hand-written, generated from a design, or migrated).

## Modular Components

Break a feature into independent files rather than one large component:

```
src/
  components/
    UserCard/
      UserCard.tsx
      UserCard.test.tsx
  hooks/
    useUserCard.ts
  data/
    mockUsers.ts
```

A component file should be readable in one pass. If it's handling data fetching, business logic, *and* rendering, split it.

## Logic Isolation

Move event handlers and business logic into custom hooks under `src/hooks/`, not inline in the component body.

```tsx
// ❌ Logic and rendering tangled together
function UserCard({ userId }: UserCardProps) {
  const [user, setUser] = useState<User | null>(null);
  useEffect(() => {
    fetch(`/api/users/${userId}`).then(r => r.json()).then(setUser);
  }, [userId]);
  // ...render
}

// ✅ Logic isolated in a hook, component only renders
function useUserCard(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  useEffect(() => {
    const controller = new AbortController();
    fetch(`/api/users/${userId}`, { signal: controller.signal })
      .then(r => r.json())
      .then(setUser);
    return () => controller.abort();
  }, [userId]);
  return user;
}

function UserCard({ userId }: UserCardProps) {
  const user = useUserCard(userId);
  // ...render only
}
```

## Data Decoupling

Static text, image URLs, lists, and other fixture-like data belong in a dedicated data module (e.g. `src/data/`), not hardcoded inline in JSX. This keeps components focused on structure/behavior and makes content easy to update or localize later.

## Type Safety

Every component takes a typed props interface, named `[ComponentName]Props`, marked `Readonly`:

```tsx
interface UserCardProps {
  readonly userId: string;
  readonly onSelect?: (id: string) => void;
}

function UserCard({ userId, onSelect }: UserCardProps) {
  // ...
}
```

## Styling

- Prefer theme-mapped classes/tokens (e.g. a Tailwind theme config, CSS variables, or a design-token system) over arbitrary hardcoded hex values or magic numbers.
- If the project has an existing style guide or theme config, sync new styles against it rather than introducing one-off values.

## Project Fit

Match the target project's existing conventions (file naming, folder layout, import aliases) rather than imposing a new structure wholesale. These rules describe the shape to aim for, not a rigid template to force onto an established codebase.
