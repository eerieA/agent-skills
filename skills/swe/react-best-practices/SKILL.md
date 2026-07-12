---
name: react-best-practices
description: Use when creating new React components, implementing hooks or state management, or reviewing React/TypeScript code (.jsx/.tsx) for quality. Covers component architecture, hooks, state management (Context, Redux Toolkit, TanStack Query), performance, Server Components (Next.js App Router), testing, and UI/interaction polish.
metadata:
  domain: frontend
  scope: implementation, review
  output-format: code
---

# React Best Practices

Senior-level guidance for building and reviewing production React + TypeScript applications.

**Assumptions:** TypeScript by default (all examples are typed). TanStack Query, TanStack Virtual, and Redux Toolkit are *recommended defaults* where they fit — not requirements; documented fallbacks apply when a project doesn't use them.

## When to Use This Skill

- Creating a new React component or feature
- Implementing or refactoring hooks
- Choosing or implementing state management (local, Context, Redux Toolkit, TanStack Query)
- Reviewing React/TypeScript code for correctness, structure, or quality
- Working with Next.js App Router Server Components / Server Actions
- Optimizing render performance
- Writing tests for components or hooks

Not every task needs every module below — load only what's relevant to the current file(s).

## Core Workflow

1. **Understand the shape of the work** — is this a new component, a hook, a state-management decision, a performance fix, or a review pass?
2. **Apply architecture rules** (`modules/architecture.md`) — file layout, logic isolation, typed props, data decoupling.
3. **Pick the right state tool** (`modules/hooks-and-state.md`) — don't reach for Redux Toolkit when `useState`/Context is enough; don't hand-roll data fetching when TanStack Query fits.
4. **Implement** with TypeScript, proper typing, and hook rules respected.
5. **Consider performance** (`modules/performance.md`) only where profiling or obvious risk (large lists, expensive renders) justifies it — don't pre-optimize.
6. **Consider UI/interaction polish** (`modules/ui-interaction-guidelines.md`) for anything user-facing: forms, focus, animation, accessibility.
7. **Validate** — run `tsc --noEmit`; fix all type errors before proceeding.
8. **Test** non-trivial logic (`modules/testing.md`) with React Testing Library.

## Module Guide

Load detailed guidance based on context:

| Topic | Module | Load When |
|-------|--------|-----------|
| Architecture & file structure | `modules/architecture.md` | Creating new components/features, organizing a module |
| Hooks & State Management | `modules/hooks-and-state.md` | Custom hooks, useEffect, Context, Redux Toolkit, TanStack Query |
| Performance | `modules/performance.md` | memo, lazy, virtualization, re-render issues |
| Server Components | `modules/server-components.md` | Next.js App Router only — RSC, Server Actions, `use client` |
| Testing | `modules/testing.md` | React Testing Library, mocking, hook tests |
| Class → Modern Migration | `modules/migration-class-to-modern.md` | Converting legacy class components |
| UI & Interaction Guidelines | `modules/ui-interaction-guidelines.md` | Forms, accessibility, animation, layout, visual/content polish |

## Constraints

### MUST DO
- Use TypeScript with strict mode; every component has a typed, `Readonly` props interface
- Break features into small, independent files — not large single-file components
- Move business logic and event handlers into custom hooks; keep components focused on rendering
- Move static text, mock data, and lists out of component files
- Use `key` props correctly (stable, unique identifiers — never array index for dynamic lists)
- Clean up effects (return a cleanup function for subscriptions, timers, listeners)
- Use semantic HTML and ARIA for accessibility
- Memoize callbacks/objects only when passed to memoized children or genuinely expensive
- Use Suspense boundaries for async operations
- Use `tsc --noEmit` to validate before considering work done

### MUST NOT DO
- Mutate state directly
- Create functions or objects inline in JSX when passed to memoized children
- Skip `useEffect` cleanup (memory/listener leaks)
- Chain `requestAnimationFrame`/`setTimeout` to guess at layout timing — subscribe to a real signal (`useLayoutEffect` keyed to the measured value, `ResizeObserver`, or the virtualizer's measurement API)
- Ignore React Strict Mode warnings
- Reach for Redux Toolkit or TanStack Query when local state/Context is sufficient
- Mix Server Component and Client Component concerns (hooks/browser APIs in a Server Component)
- Ship a component without considering its empty, loading, and error states

## Output Expectations

When implementing a feature, provide:
1. Component/hook file(s) with complete TypeScript types
2. A test file if the logic is non-trivial
3. A brief note on key decisions (state approach chosen, why, any tradeoffs)

When reviewing code, flag violations of the constraints above and cite the specific `modules/` rule.
