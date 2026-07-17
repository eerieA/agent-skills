---
name: ui-style-guide
description: >
  Systematize a project's visual language into a shareable style guide and, when
  the project warrants it, a design system. Turns a resolved look — from the
  ui-taste skill, an existing product, or the user's own tokens — into a
  structured artifact: a token taxonomy (color roles, a type scale with
  size/line-height, spacing, radius, elevation), a component inventory that shows
  every component in every state (default, hover, focus, active, disabled, error,
  loading, empty), and grid/spacing/iconography specimens, laid out as an indexed
  reference document. Also judges *whether a project needs a system at all* vs. a
  lightweight guide, and how to name, structure, and govern one. Use when asked to
  "make a style guide", "build a design system", "document our UI", "define design
  tokens", "create a component library spec", or to standardize an existing
  interface for consistency and reuse. Takes the aesthetic as input and
  systematizes it — it does not decide the look (that is ui-taste). Self-contained;
  composes with ui-taste and ux-principles if present.
metadata:
  domain: uiux
  scope: design
  output-format: artifact
---

# Style Guide & Design System

This skill produces a **specification**, not a styled screen. Its output is the
document and inventory a team designs *against*: the tokens named and tabulated,
every component drawn in every state, the grid and spacing shown as measured
specimens, the whole thing indexed so anyone can find "what's our error color" or
"what does a disabled secondary button look like" in seconds.

Two things separate this from just styling an interface:

1. **It systematizes an existing decision; it doesn't make a new one.** The
   *look* — concept, palette, personality — comes in as input (from `ui-taste`,
   from an existing product, or from the user). This skill's job is to name it,
   structure it, cover every state, and make it reusable. If no coherent look
   exists yet, that is a `ui-taste` job first (see boundaries below).
2. **Completeness is the product.** A style guide that shows a button but not its
   disabled and loading states, or a color but not its role and contrast pairing,
   has failed at its one job. The value is in the coverage, not the prettiness.

## When to Use This Skill

- "Make a style guide", "build/start a design system", "document our UI".
- "Define our design tokens", "create a component library spec", "standardize the
  UI for consistency / for the dev team".
- Onboarding a team onto a shared visual language; auditing an inconsistent product
  and codifying what it *should* be.

**When to defer or redirect instead:**

- **No coherent look exists yet** → that is `ui-taste` first. You cannot
  systematize a language that hasn't been decided. Resolve the visual language
  there, then return here to document it. (If both are needed, do them in that
  order.)
- **The project is too small to warrant a system** → say so (see §1). A one-page
  site or a throwaway prototype needs a short token list, not a governed system.
  Over-systematizing is a real failure mode.
- **A mature official design system already fits** (Material, Fluent, Carbon,
  Polaris, Atlassian, USWDS) → adopt and document *deltas* from it; don't rebuild
  it. One system per project.
- **Whether the design *works* or *looks good*** → `ux-principles` (behavior,
  flows, cognitive load) and `ui-taste` (aesthetic quality) respectively. This
  skill assumes both are settled and captures the result.

## Step 1 — Decide the Altitude (Guide vs. System vs. Neither)

Match the artifact to the project; do not default to "full design system."

- **Token sheet** (smallest) — a one-screen palette + type + spacing summary. For
  small sites, single surfaces, prototypes. Often this is all that's needed.
- **Style guide** (the common case) — tokens **plus** a component inventory with
  full state coverage, grid/spacing/iconography specimens, indexed. This is what
  the two reference examples show; it is the default target of this skill.
- **Design system** (largest) — a style guide **plus** governance: naming
  conventions, contribution/versioning process, usage documentation ("do/don't"),
  code-token linkage, and an ownership model. Justified only when *multiple
  teams/products* share the language and it will *evolve over time*.

Decide from real signals: number of surfaces, number of people building, expected
lifespan, and how much reuse actually recurs. A design system exists to *stop
inconsistency at scale* — if there's no scale, it's overhead. State the altitude
you chose and why in one line before building.

## Step 2 — Establish the Source of Truth (Input)

Systematize a language; don't invent one here. Resolve where the look comes from:

1. **From `ui-taste`** — a resolved style contract (governing concept, palette,
   type, shape, density, motion, elevation). Ideal input: it maps almost directly
   to tokens. Carry the **governing concept** into the guide as its opening
   statement — it's the "why" behind every token.
2. **From an existing product** — audit the live UI and *extract* the de-facto
   tokens (the real colors/sizes in use), then rationalize them (collapse the 11
   near-identical greys into 5 named steps). Flag drift and inconsistency as
   findings; the guide is the corrected target, not a transcript of the mess.
3. **From the user directly** — they hand over colors/fonts/rules. Capture and
   structure them; fill gaps by asking, not by silently inventing.

If the input is incoherent or missing, stop and route to `ui-taste` — see the
boundary above. Do not paper over an undecided look with a nice-looking token sheet.

## Step 3 — Build the Token Taxonomy

Tokens are named decisions. Name by **role**, not by literal value — `color-danger`
not `red-500`, so the meaning survives a value change. Cover:

- **Color** — grouped by role, the way both reference guides do it:
  - **Brand** — primary, secondary (the identity colors).
  - **State / semantic** — success, warning, error, info (reserved; never reused as
    brand accent — an error must always read as an error).
  - **Neutral / base** — 4–6 steps from background to primary text (off-black/
    off-white; warm or cool held consistently).
  - Each swatch carries its **hex + the role + at least one AA-valid text pairing**.
    A color in a guide without its contrast pairing is incomplete.
- **Typography** — the family, and a **scale table** with, per level (display, H1–H4,
  body, caption, label): font size, line height, weight, and letter-spacing. The
  reference guides show size + line-height per level explicitly — match that rigor.
  Separate headline vs. body families if the language uses two.
- **Spacing** — a base unit (4 or 8px) and the step scale, shown as measured
  specimens (a row of gaps labeled 4/8/12/16/24/32/48…). Spacing is a token, not a
  vibe.
- **Radius** — the corner-radius scale and where each step applies.
- **Elevation** — the shadow/border/background-shift levels and what each signifies.
- **Grid** — the column system(s) per breakpoint, gutters, margins, max content
  width. (This is the *mechanical* grid the ui-taste style packs deliberately leave
  out — it belongs here, tied to breakpoints.)
- **Iconography** — the icon family, sizes offered (`e.g.` 16/20/24/40), and stroke/
  weight rules. One family.

Present tokens as **reference tables/specimens**, not prose — the guide is looked up,
not read.

## Step 4 — Build the Component Inventory (the core deliverable)

This is where most guides earn or lose their value. For every component the product
uses, show it in **every state it can occupy** — this is the single most important
discipline of the skill, and the most common thing done incompletely.

- **Interactive components** (button, input, select/dropdown, checkbox, radio,
  toggle, tab, link) — show: **default, hover, focus (visible ring), active/pressed,
  disabled**, and where applicable **filled + valid + error + with-icon**. The 4Paws
  reference shows inputs as empty → filled-valid(✓) → error(✗) and dropdowns as
  closed → focused → open; replicate that state-by-state completeness for each.
- **Variants** — primary/secondary/tertiary, sizes (sm/md/lg), with/without icon —
  in a labeled matrix, not scattered one-offs.
- **Composite components** (cards, tables, modals, banners, forms, nav) — show the
  real composition and its key states (`e.g.` table: header, row, hover-row,
  selected, empty, loading; card: default, hover, with-media, with-actions).
- **Anatomy** — for non-trivial components, label the parts and their token usage
  (padding = space-4, radius = radius-md, border = neutral-2) so the spec is
  buildable, not just viewable.

Every component must be composed **from the tokens** in Step 3 — that traceability
is what makes it a system rather than a mood board. If a component needs a value
that isn't a token, either add the token or fix the component; never hardcode.

## Step 5 — Structure and Present the Artifact

The reference examples are **indexed, sectioned documents**. Structure yours the same
way so it's navigable:

- **Index / contents** up front (Colors, Typography, Iconography, Grid, Spacing,
  then each component group). Number the sections.
- **Open with the governing concept / brand statement** — one or two lines on what
  the language is *for*. This is the "why" that keeps future additions coherent.
- **One concern per section**, tokens as tables/specimens, components in state
  matrices, generous labeling.
- **Usage notes where they prevent misuse** — a short do/don't on the things people
  get wrong (when to use secondary vs. tertiary button; never put body text on the
  brand color). Full do/don't governance is a *design-system* altitude concern; a
  plain style guide can keep this light.

For a rendered/shareable output, an **Artifact** (self-contained HTML page) is the
natural medium — it can *live-render* every token and component in every state,
which is exactly what a style guide is for. Match the guide's own tokens when
building it. See the skill's `templates/` for the section/inventory skeleton.

## Step 6 — Accessibility Floor (shared invariant)

Same hard floor as the sibling skills, and a style guide is the right place to
*prove* it: **WCAG AA** — 4.5:1 body, 3:1 large text and meaningful UI. Every color
pairing in the palette section, and every component state (especially disabled,
placeholder, focus ring, and text-on-accent), must be shown against its real
background with its contrast holding. A guide that ships an inaccessible token has
codified a bug for the whole team to reuse. Focus states are mandatory in the
inventory, not optional.

## Relationship to Other Skills

Self-sufficient; composes if the others are present.

- **`ui-taste`** — decides the **look** (governing concept, palette harmony,
  personality, style contract). This skill takes that as input and **systematizes**
  it into tokens + inventory + doc. Clean directional pipeline:
  *ui-taste resolves the language → ui-style-guide documents and componentizes it →
  screens are built against the guide.* If the look isn't resolved, go there first.
- **`ux-principles`** — decides whether the interface **behaves** well (flows,
  hierarchy logic, interaction-state *requirements*). This skill captures the
  resulting states as an inventory; the *reason* a state exists is a UX concern.
- **A framework/component skill** (React, a design-system library) — owns how the
  inventory becomes real code (component APIs, token wiring). This skill specifies
  *what* to build and *in what states*; that skill owns *how*.

## Pre-Flight Check

Run before delivering. If a box can't be honestly ticked, it isn't done.

- [ ] **Altitude declared** (token sheet / style guide / design system) and matched
      to real project scale — not over-systematized
- [ ] **Source of truth** established (ui-taste contract / audited product / user
      input); no silently invented look
- [ ] **Governing concept / brand statement** opens the guide
- [ ] **Tokens named by role**, tabulated; color swatches carry hex + role + AA text
      pairing; type scale shows size + line-height + weight per level; spacing/radius
      shown as specimens
- [ ] **Component inventory covers every state** — default, hover, focus (visible
      ring), active, disabled, error, loading, empty — for every interactive and
      composite component; variants in a labeled matrix
- [ ] **Every component composed from tokens** — no hardcoded off-token values
- [ ] **Indexed and sectioned**, one concern per section, looked-up not read
- [ ] **AA proven** on every pairing and every state, against real backgrounds
- [ ] **Deferrals honored** — official system adopted (not rebuilt) if one fits;
      undecided look routed to ui-taste; small project not over-systematized
