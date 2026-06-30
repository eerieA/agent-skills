---
name: gql-frontend-arch
description: Architecture guidance for building a frontend web application that consumes a GraphQL backend and is used collaboratively by a small team. Covers module boundaries, state and data-fetching strategy, where domain logic should live, the boundary/seam between the app and its API, routing structure, tabular data UIs, forms, error handling, performance budgets, and testing strategy. Use this skill whenever the user is designing, refactoring, or making structural decisions about a frontend web app — including questions about where state or logic should live, where the boundary with the API goes, how to organize features, how to model GraphQL data on the client, how to scale tables and lists for moderate data sizes, or how to keep a growing codebase maintainable. Trigger this even when the user does not explicitly say "architecture" — questions about folder structure, "where should I put X", reusability, separation between UI and data, or decomposition all qualify.
---

# Frontend Web App Architecture

Guidance for designing the architecture of a frontend web application that talks to a GraphQL backend and is used by a small, collaborative team. The advice is tech-agnostic but assumes a modern single-page-app stack (e.g. React-family frameworks, a query/cache library, a client-side router, a table/data-grid library).

This skill is opinionated about *process* — how to decide — but tries to stay neutral about specific libraries unless the user has already named them.

## Scope

**Use this skill for:**

- Structuring a new or growing frontend codebase (module boundaries, feature folders, layering)
- Deciding where state should live (server cache, URL, local component, global client store, form state)
- Designing the data layer against a GraphQL API (query co-location, fragments, normalization, caching, mutations)
- Designing routes, layouts, and navigation
- Building viewable/editable data tables at moderate scale (thousands of rows / tens of thousands of cells, not millions)
- Forms, validation, optimistic updates
- Error, loading, and empty states; resilience against backend hiccups
- Performance budgets and rendering strategy
- Testing strategy for a frontend codebase
- Code review and refactor planning at the architectural level

**Do not use this skill for:**

- Backend service design, microservice decomposition, or data-store choices on the server
- Pure visual/UX design questions (color, typography, layout aesthetics)
- Single-line code questions or framework syntax lookups
- DevOps, CI/CD, infra provisioning

## Default assumptions

Unless the user says otherwise, assume:

- Small-to-moderate concurrent user count (collaborative internal tool, not consumer scale).
- Moderate data volumes — tables in the low thousands of rows, never millions; client can hold a working set in memory.
- A GraphQL backend that the frontend does not own; schema changes are negotiated.
- A small team (a handful of contributors) that values readability and iteration speed over premature abstraction.

Call out explicitly when a recommendation depends on these assumptions, so the user can correct you if their context differs.

## How to apply this skill

When the user asks an architectural question, work through these in order:

1. **Clarify intent.** What is the user actually trying to decide? Is this a greenfield choice, a refactor, or a "where do I put this" question? Ask at most one or two focused clarifying questions if the answer hinges on missing context; otherwise state your assumptions and proceed.
2. **Identify the layer.** Most frontend questions live in one of: routing, data layer (GraphQL + cache), state management, component composition, presentation, or cross-cutting concerns (errors, auth, perf, testing). Name the layer — it focuses the discussion.
3. **Apply the relevant decision framework below.** Walk the user through the tradeoff, not just the conclusion.
4. **Surface anti-patterns** that the proposed approach risks falling into.
5. **Keep the recommendation focused.** Three solid decisions the user will actually follow beats a ten-section document they won't read.

---

## Architectural layers (mental model)

A useful mental model for this kind of app — not a strict prescription:

- **Routing / shell layer.** URL → view. Owns layouts, route-level data loading, route-level error and auth boundaries.
- **Feature modules.** Each major user-facing capability (e.g. "devices", "topology", "jobs") is a self-contained folder with its own routes, queries, components, and types. Features depend on shared primitives, not on each other. Aim for a **consistent internal layout across features** — when every feature puts its types, validation, operations, derived state, and components in predictably-named places, a contributor who knows one feature knows them all. Don't over-formalize the filenames, but don't let each feature invent its own structure either.
- **Data layer.** GraphQL operations (queries, mutations, subscriptions/fragments), the query cache, and the small amount of code that adapts server data into shapes the UI wants. This is the boundary between "what the server says" and "what the UI needs".
- **UI primitives.** Generic, presentational components — buttons, inputs, modals, table cells, layout helpers. No business logic, no data fetching.
- **Domain types and logic.** Pure functions and types that encode rules about your domain (e.g. "a device is reachable when X"). Framework- and UI-free, so they're easy to test.
- **Cross-cutting.** Auth, error reporting, feature flags, telemetry, theming.

The healthiest dependency direction is: routing → features → (data layer, domain logic, UI primitives) → cross-cutting. Features should not import from other features.

---

## Decision frameworks

### Where should this state live?

Walk down this list and stop at the first match:

1. **Is it server data?** Live in the GraphQL cache (TanStack Query, Apollo, urql, Relay — whatever the project uses). Do not mirror it into a separate client store.
2. **Should it survive a refresh or be shareable via link?** Live in the URL (route params, search params). Filters, sort order, pagination cursors, selected tab — these usually belong here.
3. **Is it form state?** Live in a form library's state (React Hook Form, TanStack Form, Formik, etc.), not in a global store.
4. **Is it ephemeral UI state for one component or its immediate children?** Local component state.
5. **Is it cross-cutting and genuinely global?** (current user, theme, feature flags, a global toast queue.) A small context or lightweight store.
6. **Only if none of the above fit** — reach for a general-purpose client state library.

Anti-pattern: putting server data into a global client store and trying to keep it in sync manually. The query cache is the source of truth; treat it that way.

### Where should this *logic* live?

The sibling of the state question. State has a home; so does each piece of logic. Walk down and stop at the first match:

1. **Does it *decide* something about the domain?** (Is this input valid against a business rule? What category does this entity fall into? What's the derived value?) → a **pure function**, framework- and UI-free, living with the feature's domain types. No data fetching inside it — feed it the data it needs. These are trivially testable and never need a component to exercise.
2. **Does it *fetch, sequence, or coordinate I/O*?** (Load X, then validate, then mutate; resolve a dependent lookup before submitting.) → the **data/service layer** (a hook or service module), above the pure logic, calling into it.
3. **Does it *render or dispatch*?** → the component. Components read already-decided values and already-fetched data; they don't embed business rules.

The rule of thumb: **decisions live as low as possible; I/O lives as high as possible.** A component that fetches, applies a business rule, *and* renders is doing three layers' jobs — pull the decision down into a pure function and call it.

Anti-pattern: a business rule (eligibility, classification, a derived field) computed inline inside a presentational component or a cell renderer. It becomes untestable without mounting the component, and it gets silently re-implemented the next time the same rule is needed elsewhere. (For the disciplined, codebase-anchored version of this split, see the `noat-design-philosophy` skill.)

### Where does the boundary between my app and the API go?

For anything beyond a toy app, treat the external API as something you reach through a **single, owned seam** — not something components and features call directly. Define the shape *your app* wants (typed operations, normalized results, your own error categories), and let exactly one layer translate between that and the raw API. Everything above the seam speaks your app's language; only the seam knows the API's quirks.

This matters because every API you don't own has an awkward shape — pagination envelopes, null conventions, error formats, partial shapes. The NOAT API, for instance, returns single-object reads as one-element lists and puts error codes under `extensions.code`. If that leaks upward, every feature ends up knowing it, and the day the API changes you edit fifty files instead of one.

**When it pays** (and when it doesn't):
- **Worth it** when the app is non-trivial, you want features testable without a live backend (fake the seam, not each call site), or you anticipate the API shape shifting. The seam is what lets you inject a fake GraphQL layer in tests and normalize quirks in one place. **The skill's default audience — a small team building a growing internal tool (see Default assumptions) — is squarely in this bucket; build the seam.**
- **Overkill** for a throwaway prototype or a single-screen tool — there, calling the query hooks directly is fine; don't build a seam you won't benefit from.

Keep it lightweight, and be precise about what the seam does vs. doesn't do — this is the line that reconciles it with the data-layer section below:
- **Do** centralize *quirk normalization*: the API's transport-shaped oddities — response envelopes, one-element-list reads, `extensions.code` error formats, null conventions. These are pure mechanical translation, they recur everywhere, and they belong in one place.
- **Don't** re-model every entity into a parallel ViewModel/DTO "for flexibility." That's a different, heavier thing the data-layer section warns against — add a per-entity adapter only when a specific shape is genuinely awkward (deeply nested, connection edges to flatten), not by default.

So: one place normalizes the *quirks* for everything; per-entity *reshaping* stays the exception. Stay neutral on mechanism — co-located typed operations + a small shared normalization step is usually enough.

Anti-patterns:
- Components or feature code that destructure API-shaped quirks directly (`data.things[0]`, `error.extensions.code`) — that knowledge leaked past the seam.
- A "seam" so thick it re-models every entity into a ViewModel "for flexibility" before there's a second consumer. (See the `noat-design-philosophy` skill for the disciplined single-chokepoint version — *seal the messy shape in one place*.)

### How should I shape the GraphQL data layer?

A useful default structure:

- **Co-locate operations with the feature** that uses them. A `devices/` feature folder owns its `devices.graphql` (or `.ts` with `gql` tagged templates).
- **Use fragments for reusable shapes**, especially for entities that appear in multiple views (e.g. a `DeviceSummary` fragment used by both the list and the detail page). Fragments are the GraphQL-native way to keep queries DRY without coupling features to each other.
- **Generate types from the schema** (GraphQL Code Generator or equivalent). Hand-written types for server data drift and lie.
- **Keep a thin adapter layer** between raw query results and what components consume *only when* the server shape is awkward (e.g. deeply nested, has connection edges you want to flatten). Do not build a full DTO/ViewModel layer by default — it's usually overhead for a frontend app of this size. (This is distinct from *quirk normalization* — envelopes, error formats, null conventions — which the API-boundary section above centralizes in the seam for everything. Normalize quirks once; reshape individual entities only as the exception.)
- **Mutations should update the cache explicitly**: either via the library's normalized cache updates, or by invalidating the relevant queries. Pick one strategy per feature and stick to it.
- **Subscriptions or polling** for live-ish data: choose based on backend capability. If the backend supports subscriptions and the data really changes mid-session (job status, alerts), use them. Otherwise interval refetch on the affected query is simpler and good enough.

Anti-patterns to flag:
- One giant query that fetches everything for a page just to "avoid waterfalls" — leads to over-fetching and brittle caching. Prefer multiple smaller queries that compose via fragments, unless you have measured a real waterfall problem.
- Querying inside deeply nested presentational components. Queries belong near route or feature boundaries; pass data down.
- Bypassing the cache with raw `fetch` calls for "just this one thing".

### How should I organize routes?

- **Route structure mirrors the user's mental model**, not the backend's schema. If the user thinks "devices → device detail → interfaces tab", that's the URL shape.
- **Load data at the route level** when the library supports it (TanStack Router loaders, Remix-style loaders, route-level queries). This makes loading and error boundaries predictable and avoids "flash of empty state" inside deeply nested components.
- **Search params for view state**: filters, sort, pagination, selected row id. They become free undo/redo, free deep-linking, and free shareable URLs.
- **Layout routes for shells** (sidebars, headers, auth gates) so they don't re-mount on navigation between siblings.

Anti-pattern: encoding important view state (active tab, selected filters) only in component state, so refreshing the page loses it and links can't be shared with teammates.

### How should I decompose components?

A few heuristics, in rough priority order:

1. **Split by responsibility, not by size alone.** A 200-line component that does one coherent thing is fine. A 60-line component that mixes data fetching, business rules, and presentation is not.
2. **Separate "container" concerns from "presentational" concerns** where it adds clarity. The component that calls `useQuery` and decides what to do with loading/error states is different from the one that renders the rows. You don't need a strict pattern — just notice when one component is doing both jobs awkwardly.
3. **Lift state up only as far as needed.** Don't hoist state to a parent that doesn't need to know about it.
4. **Name components for their domain role**, not their visual role. `DeviceStatusBadge` ages better than `GreenPill`.
5. **A file getting long is a smell, not a rule.** Split when there's a natural seam, not at an arbitrary line count.

### How should I handle data tables?

Tables are often the heart of internal tools. For moderate row counts (working set fits comfortably in memory):

- **Server-side pagination, filtering, and sorting** if the dataset can exceed what you want to ship to the client in one go, *or* if multiple users need consistent views. Encode the table state in URL search params so it round-trips.
- **Client-side pagination/sort/filter** is fine — and simpler — when the full working set is already loaded for other reasons and stays modest in size.
- **Virtualization (windowing)** becomes worth it once rendered row counts get into the low thousands or rows are visually heavy. For a few hundred rows, virtualization is usually unnecessary complexity.
- **Column definitions are data**, not JSX. Define columns as an array of typed config objects so they can be reused, reordered, persisted as user preferences, and tested.
- **Selection, expansion, and editing state** belong in table state (the table library's state or a small reducer next to it), not scattered across cell components.
- **Cell editing** that hits the backend: prefer optimistic updates with rollback on error, and debounce/coalesce rapid edits.

Anti-patterns:
- Reaching for virtualization before there's a measured rendering problem.
- Re-implementing sorting/filtering/pagination logic per table instead of leaning on the table library.
- Embedding business logic in cell renderers (e.g. "if status is X and user role is Y, show edit button"). Compute that in the row's view model.

### How should I handle forms?

- **Use a form library** for anything beyond a single input. Manual `useState` for every field plus manual validation is the path to bugs.
- **Validate with a schema** (Zod, Yup, Valibot) and share that schema between client and — where possible — the GraphQL input type. Generated types help here.
- **Submit = mutation.** Show pending, success, and error states from the mutation, not from a separate piece of state you're trying to keep in sync.
- **Optimistic updates** when the success case is overwhelmingly likely and rollback is cheap (toggles, renames). Avoid them for actions with side effects users would notice if rolled back.

### How should I handle errors, loading, and empty states?

- **Three states per data view, minimum:** loading, error, empty. Treat "empty" as a designed state, not a bug — what should the user do next?
- **Error boundaries at route level** catch render-time errors and prevent the whole app from white-screening. Wrap risky regions (an embedded chart, a third-party widget) in their own boundary.
- **Network/GraphQL errors** are not render errors — surface them inline in the component that triggered them (a toast for mutations, an inline message for queries), with a retry affordance where it makes sense.
- **Don't swallow errors.** If you catch, either handle visibly or report to your error tracker. Silent catches hide real problems for weeks.

### What about performance?

For an app of this scale, you almost certainly do *not* have a performance problem — until you do, in one specific place. Don't pre-optimize. But do:

- **Set a budget** for initial bundle size and time-to-interactive on the main routes. Measure it in CI if you can.
- **Code-split by route** so logging in doesn't ship the admin panel.
- **Memoize selectively**, when the profiler shows a real cost. `useMemo` and `React.memo` everywhere is noise and can even slow things down.
- **Move expensive computations into the data layer** (selectors, derived fields computed once when data lands in the cache) rather than recomputing per render.
- **Profile before refactoring for perf.** "It feels slow" is a starting point, not a diagnosis.

### How should I test this?

A balanced pyramid for a frontend app of this kind:

- **Unit tests** for domain logic and pure utilities — fast, plentiful, no DOM.
- **Component tests** (Testing Library style) for components with meaningful behavior — forms, tables, anything with conditional rendering. Test through the user's eyes (roles, text), not implementation details.
- **Integration tests at the feature level** with a mocked GraphQL layer (MSW or the library's testing utilities) — these catch most real regressions.
- **A small number of end-to-end tests** for critical user journeys only (login, the one or two flows the business absolutely depends on). E2E is expensive; spend it where it matters.

Anti-patterns:
- Snapshot tests on large components — they fail loudly on harmless changes and rarely catch real bugs.
- Mocking your own modules to test your own modules. If you need to mock heavily, the seam is probably in the wrong place.

---

## Cross-cutting anti-patterns to watch for

Independent of any one decision, flag these whenever they appear:

- **Generic dumping-ground modules** — `utils/`, `helpers/`, `common/`, `shared/` with no theme. Either give the module a real name (`formatBytes` lives in `formatting/`, `parseDeviceId` in `devices/`), or let the function live next to its one caller.
- **Premature abstraction.** A "reusable" component used in exactly one place is just an indirection. Wait for the third use before extracting.
- **Speculative layering.** ViewModels, mappers, and adapters introduced "for flexibility" before there's a concrete second use case. Add layers when the pain of not having them shows up.
- **Cross-feature imports.** `features/devices` importing from `features/jobs` quietly turns into a tangle. Move the shared thing into `shared/` or a clearly-named module.
- **Stringly-typed APIs.** Magic strings for statuses, roles, kinds. Use union types or enums; let the compiler help.
- **Hidden coupling through global stores.** If feature A writes to a global store and feature B reads from it, that's an undocumented contract. Prefer explicit props, URL state, or a shared query.
- **Re-implementing the framework.** Custom routers, custom data caches, custom form state — almost always a sign that an existing library was not understood, not that it was inadequate. Check first.
- **Inconsistent error handling per feature.** Pick a convention (where errors surface, what gets retried, what gets logged) and apply it everywhere.

---

## Output expectations

When responding to architecture questions, structure the answer roughly like this:

1. **One- or two-sentence recommendation up front.** The user should know what you think before reading the rationale.
2. **The tradeoff you considered.** What was the alternative, and why is the recommendation better *for their situation*?
3. **Concrete next steps.** Folder names, library shapes, the actual hook signature — not just patterns in the abstract. Stay neutral about library choice unless the user has named one.
4. **What *not* to build.** Call out things the user might be tempted to add that aren't worth it yet at their scale.
5. **A success signal.** How will the user know in a month whether this decision worked? (e.g. "if you find yourself adding a third `useEffect` to keep these in sync, the boundary is wrong.")

Keep it focused. Three good decisions beat a ten-page treatise.