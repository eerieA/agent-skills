# Server Components

> **Applies only to Next.js App Router projects.** If this project is a client-only SPA (Vite, CRA, plain React), skip this file entirely — there is no Server Component runtime.

## Server vs Client Components

```tsx
// Server Component (default in App Router)
// Can: fetch data, access backend, use async/await
// Cannot: use hooks, browser APIs, event handlers
async function ProductList() {
  const products = await db.products.findMany();
  return <ul>{products.map(p => <ProductCard key={p.id} product={p} />)}</ul>;
}

// Client Component (explicit)
'use client';
import { useState } from 'react';

function AddToCartButton({ productId }: { productId: string }) {
  const [loading, setLoading] = useState(false);
  return (
    <button onClick={() => addToCart(productId)} disabled={loading}>
      Add to Cart
    </button>
  );
}
```

## Decision Tree

- Need interactivity (onClick, state)? → Client Component
- Need browser APIs (localStorage, window)? → Client Component
- Need effects or hooks? → Client Component
- Fetching data, reading files, database access? → Server Component
- SEO-critical content? → Server Component
- Large dependencies you don't want in the client bundle? → Server Component

## Data Fetching

```tsx
// app/products/page.tsx
export default async function ProductsPage() {
  const products = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600 },
  }).then(res => res.json());

  return <ProductGrid products={products} />;
}

// Parallel fetching — don't await sequentially when requests are independent
async function Dashboard() {
  const [user, orders, recommendations] = await Promise.all([
    getUser(),
    getOrders(),
    getRecommendations(),
  ]);

  return (
    <>
      <UserHeader user={user} />
      <OrderList orders={orders} />
      <Recommendations items={recommendations} />
    </>
  );
}
```

## Streaming with Suspense

```tsx
async function SlowComponent() {
  const data = await slowFetch();
  return <div>{data}</div>;
}

export default function Page() {
  return (
    <main>
      <h1>Dashboard</h1>
      <FastComponent />
      <Suspense fallback={<Skeleton />}>
        <SlowComponent />
      </Suspense>
    </main>
  );
}
```

## Passing Data Server → Client

Only serializable data crosses the boundary — no functions, class instances, or Dates without conversion.

```tsx
async function ProductPage({ id }: { id: string }) {
  const product = await getProduct(id);
  return (
    <div>
      <h1>{product.name}</h1>
      <AddToCartButton productId={product.id} price={product.price} />
    </div>
  );
}
```

## Server Actions

```tsx
// actions.ts
'use server';

export async function createPost(formData: FormData) {
  const title = formData.get('title') as string;
  await db.posts.create({ data: { title } });
  revalidatePath('/posts');
}

// page.tsx (Server Component)
import { createPost } from './actions';

export default function NewPost() {
  return (
    <form action={createPost}>
      <input name="title" required />
      <button type="submit">Create</button>
    </form>
  );
}
```

## Quick Reference

| Type | Can Use | Cannot Use |
|------|---------|------------|
| Server | async/await, db, fs | useState, onClick |
| Client | hooks, events, browser APIs | async component body |

| Directive | Purpose |
|-----------|---------|
| `'use client'` | Marks a client boundary |
| `'use server'` | Marks a Server Action |
| `<Suspense>` | Streaming, loading states across the server/client boundary |
