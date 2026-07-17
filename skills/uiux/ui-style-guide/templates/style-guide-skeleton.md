# Style Guide Skeleton

The section/inventory structure a style guide fills in. Copy it, delete altitudes
you don't need (a **token sheet** keeps §0–§2 only; a **style guide** does §0–§8; a
**design system** adds §9 governance). Present tokens as tables/specimens and
components as state matrices — the guide is *looked up*, not read. Every value must
trace to a token in §1; every pairing and state must clear WCAG AA against its real
background.

---

## 0. Cover / Index

- **Governing concept / brand statement** — one or two lines: what this visual
  language is *for*. (Carried over from the `ui-taste` style contract's Voice, or
  written from the audited product / user input.) This is the "why" future
  additions must stay coherent with.
- **Index** — numbered list of the sections below, so the doc is navigable.

## 1. Design Tokens

Name by **role**, not literal value (`color-danger`, not `red-500`).

### 1a. Color

| Role | Token | Hex | AA text pairing | Notes |
|---|---|---|---|---|
| Brand / primary | `color-brand-primary` | `#____` | `#____` (___:1) | primary actions |
| Brand / secondary | `color-brand-secondary` | `#____` | `#____` | |
| State / success | `color-success` | `#____` | `#____` | reserved — never brand |
| State / warning | `color-warning` | `#____` | `#____` | |
| State / error | `color-error` | `#____` | `#____` | |
| State / info | `color-info` | `#____` | `#____` | |
| Neutral 0 (bg) | `color-neutral-0` | `#____` | — | off-white, held warm/cool |
| Neutral 1–4 | `color-neutral-N` | `#____` | | steps to text |
| Neutral / text | `color-text` | `#____` | on `neutral-0` (___:1) | off-black |

### 1b. Typography

Family: **____** (headline) / **____** (body). Emphasis = same-family weight/italic.

| Level | Token | Size | Line height | Weight | Tracking |
|---|---|---|---|---|---|
| Display | `type-display` | | | | |
| H1 | `type-h1` | | | | |
| H2 | `type-h2` | | | | |
| H3 | `type-h3` | | | | |
| Body | `type-body` | ≥16px mobile | ~1.6 | | |
| Caption | `type-caption` | | | | |
| Label | `type-label` | | | | |

### 1c. Spacing

Base unit: **__px**. Scale (show as measured specimens):
`space-1 … space-N` → __, __, __, __, __, __, __ px.

### 1d. Radius

`radius-sm/md/lg/full` → __ / __ / __ / __ px. Where each applies: ____.

### 1e. Elevation

`elevation-0/1/2/…` → the shadow/border/bg-shift per level, and what each signifies.
State if hierarchy is expressed without shadow.

### 1f. Grid (mechanical — per breakpoint)

| Breakpoint | Columns | Gutter | Margin | Max width |
|---|---|---|---|---|
| mobile | | | | |
| tablet | | | | |
| desktop | | | | |

### 1g. Iconography

Family: **____**. Sizes: __ / __ / __ px. Stroke/weight rule: ____. One family only.

## 2. Foundations Recap (token sheet stops here)

A one-screen visual of palette + type + spacing for quick reference.

---

## 3–7. Component Inventory

For **each** component: show every state, compose from §1 tokens, label anatomy.

### Interactive components — state matrix per component

| Component | default | hover | focus (ring) | active | disabled | error | with-icon |
|---|---|---|---|---|---|---|---|
| Button / primary | | | | | | — | |
| Button / secondary | | | | | | — | |
| Button / tertiary | | | | | | — | |
| Text input | | | ✓ | | | ✓ | |
| Select / dropdown | closed | | focused | | | | open |
| Checkbox | | | | | | | |
| Radio | | | | | | | |
| Toggle / switch | off | | | on | | | |
| Tab | | | | selected | | | |
| Link | | | | visited | | | |

Sizes offered (sm/md/lg) and variants shown as a labeled sub-matrix, not one-offs.

### Composite components — composition + key states

- **Card** — default, hover, with-media, with-actions.
- **Table** — header, row, hover-row, selected, empty, loading.
- **Modal / dialog** — default, with-form, confirm/destructive.
- **Banner / alert** — success, warning, error, info (uses state tokens).
- **Form** — grouped fields, inline validation, submit states.
- **Navigation** — default, active item, mobile-collapsed.

### Anatomy (for non-trivial components)

Label parts and their token usage: `padding = space-4`, `radius = radius-md`,
`border = 1px color-neutral-2`, `text = type-label / color-text`. Makes the spec
buildable, not just viewable.

## 8. Usage Notes (light for a guide, expand for a system)

Short do/don't on the things people get wrong:
- When to use secondary vs. tertiary button.
- Never put body text on the brand color.
- State tokens are reserved — don't reuse error-red as an accent.

---

## 9. Governance (design-system altitude only)

- **Naming conventions** — the token/component naming scheme, spelled out.
- **Contribution & versioning** — how a new component enters; how changes version.
- **Code-token linkage** — how these tokens map to the codebase (CSS vars, theme
  file, framework tokens).
- **Ownership** — who maintains it, how deprecations are handled.
- **Full do/don't usage docs** per component.

Include §9 **only** when multiple teams/products share the language and it will
evolve — otherwise it's overhead (see SKILL.md Step 1).
