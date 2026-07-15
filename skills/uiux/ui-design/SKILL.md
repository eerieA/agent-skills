---
name: ui-design
description: >
  Anti-slop visual UI design for product and marketing surfaces — landing pages,
  portfolios, app screens, forms, and dashboards. Reads the brief and infers the
  right design direction instead of defaulting to a templated look, then builds
  interfaces around a normalized *style contract* (palette, type scale, shape,
  density, motion, elevation). The aesthetic is PLUGGABLE: pick a built-in style
  (minimalist, brutalist), describe your own in text, hand over a reference
  image/ASCII, or let the skill infer one from the brief. Enforces
  style-independent invariants — WCAG contrast, touch targets, reduced-motion,
  one-theme/one-accent/one-shape locks, real images over fake screenshots — that
  no style may override, plus a catalog of AI "tells" to avoid and a pre-flight
  check. Use when asked to build, style, or redesign an interface, choose colors
  / typography / layout / motion, or "make it look {minimalist, brutalist,
  premium, editorial, …}" and not generic. Defers dense enterprise UI to official
  design systems. Self-contained; composes with a UX or React skill if present.
metadata:
  domain: uiux
  scope: implementation
  output-format: code
---

# UI Design

This skill makes interfaces that look *designed*, not *generated*. Most AI UI
output is bad for one reason: the model jumps to a default aesthetic (AI-purple
gradients, centered hero on dark mesh, three equal feature cards, Inter +
slate-900) instead of reading the brief and committing to a real direction. This
skill's whole job is to override that reflex.

Two ideas run through everything below:

1. **The visual style is pluggable.** The look — palette, typography, shape,
   density, motion — is resolved at the start into a small **style contract**, and
   that contract can come from a named built-in, a text description, a reference
   image, or brief-inference. Minimalist and brutalist are not two different
   skills; they are two settings of this one.
2. **Invariants sit above the style.** Accessibility, consistency locks, and
   honesty rules apply *regardless* of the chosen style. A style pack configures
   the knobs; it may never turn off the guardrails.

This skill is written to be stack-agnostic. Code fragments are illustrative
(`e.g.`) — apply them in whatever framework and styling system the project uses,
matching the existing code exactly. Where a real framework is present (React,
Tailwind, a design system), use its idioms; the principles don't change.

## When to Use This Skill

- Building or styling any UI: landing/marketing pages, portfolios, app screens,
  forms, dashboards.
- Choosing palette, typography, layout, spacing, motion, or component styling.
- "Make it look {minimalist, brutalist, premium, editorial, Linear-clean, …}" — or
  "make it not look AI-generated."
- Redesigning an existing interface.

**When to defer instead:**

- **Dense enterprise UI, data tables, complex wizards, code editors, native
  mobile, realtime-collab canvases.** These have official systems and problem-class
  patterns that beat hand-rolled styling. Say so, point to the right tool (Fluent,
  Carbon, Atlassian, Polaris, Material, USWDS/GOV.UK; TanStack/AG Grid for tables;
  Monaco/CodeMirror for editors; Apple HIG / Material for native), and apply this
  skill only to the marketing/onboarding/about surfaces around them.
- **Whether the design *works*** (hierarchy logic, flows, cognitive load) — that is
  the `ux-principles` skill. This skill assumes the UX is sound and makes it look
  and feel right.

## Step 0 — Read the Brief Before Touching Anything

Do not generate until you have inferred what the user actually wants. Read these
signals:

- **Surface kind** — landing (SaaS / consumer / agency / event), portfolio, app
  screen, form, dashboard, editorial/blog, redesign.
- **Vibe words** the user used — "minimalist", "calm", "Linear-style", "brutalist",
  "premium", "playful", "editorial", "serious B2B", "dark tech".
- **Reference signals** — URLs, screenshots, products or competitors named.
- **Audience** — who decides the aesthetic (a procurement panel vs. a
  design-conscious consumer vs. a recruiter). The audience picks the style, not
  your taste.
- **Existing brand assets** — logo, color, type, imagery. For redesigns these are
  starting material, not optional (see §5).
- **Quiet constraints** — accessibility-critical, public-sector, regulated,
  trust-first, kids'. These override aesthetic preference.

**Output a one-line Design Read before any code:**
> *"Reading this as: {surface} for {audience}, with a {vibe} language, resolving to
> {style source}."*

If the brief is genuinely ambiguous *and* the read could diverge, ask **one**
question — never a dump. Otherwise declare the read and proceed.

## Step 1 — Resolve the Style Contract (The Pluggable Part)

Every project resolves to exactly one **style contract**: a normalized token set
the rest of the work reads from. Resolve it from the highest-priority source the
brief provides:

1. **Named built-in style** — user names one ("use minimalist" / "brutalist").
   Load `styles/<name>.md` and use its contract.
2. **User-described style** — free text ("warm, calm, lots of whitespace, serif
   headers, barely-there motion"). Synthesize a contract from the description using
   the `styles/_template.md` schema, then **echo it back in one block for
   confirmation** before building.
3. **Reference image / ASCII / linked site** — extract the contract from it:
   palette, type feel, shape/radius, density, motion, elevation. Echo back what you
   extracted so the user can correct it.
4. **Infer from the brief** — no style given. Infer a direction from the Design
   Read, declare it explicitly (per Step 0), and default the knobs sensibly.
   *Never* silently fall back to the AI-default aesthetic.

### The style contract schema

Whatever the source, normalize to these tokens (full schema and authoring guide in
`styles/_template.md`):

- **Palette** — neutrals (4–5 steps), one accent (max), semantic states; light and
  dark values. Off-black/off-white, never pure `#000`/`#fff`.
- **Typography** — display face + body face (+ mono if needed), a type scale
  (ratio-based), tracking/leading rules.
- **Shape** — corner-radius scale (all-sharp / all-soft / all-pill), border weight,
  divider style.
- **Density** — spacing scale and how airy vs. packed the layout runs.
- **Motion** — intensity band (static → choreographed), default easing/duration,
  what may move and why.
- **Elevation** — how hierarchy is shown: shadows, borders, or pure spacing.
- **Imagery** — photography/illustration treatment; icon family and stroke weight.

Once resolved, the contract is **locked for the whole surface**. Every section
reads the same tokens (see the consistency locks below).

### Built-in styles

- `styles/minimalist.md` — warm monochrome, editorial, flat, generous whitespace,
  typographic contrast, near-zero shadow.
- `styles/brutalist.md` — raw Swiss-industrial *or* tactical-terminal; rigid grids,
  extreme type-scale contrast, utilitarian color, no radius, analog texture.
- `styles/_template.md` — the empty contract schema. Copy it to author a new style,
  or to capture a described/image-derived style in a consistent shape.

## Step 2 — The Style-Independent Invariants

These hold no matter what style is loaded. A style pack sets values *within* these
constraints; it never relaxes them.

### Accessibility (hard floor)
- **Contrast** WCAG AA: 4.5:1 body, 3:1 large text and meaningful UI. Audit *every*
  button, input, placeholder, focus ring, and label against its actual background —
  no white-on-white CTAs, no ghost buttons unreadable over photos (add a scrim).
- **Touch targets** ≥ 44×44 px with spacing between them.
- **Keyboard + focus** — everything operable by keyboard with a visible focus state.
- **Reduced motion** — anything beyond a hover/press must honor
  `prefers-reduced-motion` and collapse to static. Non-negotiable.

### Consistency locks (audit before shipping)
- **Theme lock** — one theme (light / dark / auto) for the whole surface. No section
  flips to inverted mode mid-scroll unless the brief explicitly calls for one
  deliberate, transitioned switch.
- **Color lock** — one accent, used identically across every section. No surprise
  blue CTA on a warm-grey page.
- **Shape lock** — one corner-radius system. Mixed radii are allowed only under a
  documented rule ("buttons pill, cards 16px, inputs 8px") followed everywhere.
- **Type lock** — the resolved type scale and pairing, applied consistently; no
  random mixed-family emphasis (emphasize with italic/bold of the *same* family).

### Honesty and materiality
- **Real images over fake UI.** Use a generated/real image, or `picsum.photos`
  seeded placeholders, or an explicit labeled placeholder slot. **Never** build
  fake product screenshots out of styled `<div>` rectangles — the #1 AI tell.
- **Real logos** for social proof (Simple Icons / devicon / a generated monogram),
  not plain text wordmarks; logo wall = logos only, no category labels.
- **Elevation communicates real hierarchy** — cards only when elevation means
  something; otherwise group with borders, dividers, or space. Tint shadows to the
  background; no pure-black drop shadows on light.
- **If the brief names an official design system**, install and use the *official*
  package; don't recreate its CSS or import its tokens then override 90%. One
  system per project.

### Interaction states (never ship only the happy path)
Loading (skeletons matching final layout), empty (composed, says how to populate),
error (inline/contextual, specific), success, disabled — for every interactive
surface. Tactile press feedback (`e.g.` `scale-[0.98]` or a 1px translate on
`:active`).

## Step 3 — Anti-Slop Discipline (Override the Defaults)

The model defaults to clichés when it tries to "look designed." Treat these as
banned unless the brief explicitly asks for one.

- **No AI-default aesthetic** — no auto AI-purple/blue glow gradients, no centered
  hero over dark mesh as a reflex, no three-identical-feature-cards row, no generic
  glassmorphism on everything, no Inter + slate-900 by default.
- **No em-dash (`—`) or en-dash-as-separator (`–`) anywhere visible** — headlines,
  labels, body, quotes, captions, buttons, alt text. Use a period, comma,
  parentheses, colon, or a spaced hyphen. This is the single most common AI tell.
- **No decorative filler** — section-number eyebrows (`001 · Capabilities`), scroll
  cues ("↓ scroll"), version stamps (`v0.6`, `BETA`) in heroes, locale/weather
  strips, rotated vertical text, decorative status dots, middle-dot separators
  spammed across every line, `border-t`+`border-b` on every row of a long list.
- **Eyebrow restraint** — at most ~1 uppercase-tracking eyebrow per 3 sections;
  often the headline alone is enough.
- **Layout variety** — no more than 2 consecutive image+text "zigzag" sections; a
  multi-section page uses several different layout families, not one repeated.
- **Content honesty** — no "John Doe"/"Acme"/"Lorem Ipsum"; no fake-precise metrics
  presented as real; no filler verbs ("Elevate", "Seamless", "Unleash",
  "Next-Gen", "Revolutionize"). Re-read every visible string before shipping and
  cut anything grammatically broken or AI-cute.
- **Icons from a real library** (Phosphor / HugeIcons / Radix / Tabler), one family,
  standardized stroke; never hand-roll SVG icon paths.

## Step 4 — Motion and Responsive (Craft Layer)

**Motion must be motivated.** Before adding any animation, name what it
communicates: hierarchy, storytelling, feedback, or state transition. "It looked
cool" is not a reason. If you can't state the reason in one sentence, drop it.

- Animate **only `transform` and `opacity`** (GPU-friendly); never `width`,
  `height`, `top`, `left`, `margin`. Reserve space to avoid layout shift.
- **Timing** (defaults; the style contract may tighten): micro-interactions
  100–150 ms, state changes 200–300 ms, page/modal transitions 300–500 ms. Ease-out
  for entrances, ease-in for exits, ease-in-out for transitions; avoid linear except
  continuous loops.
- **No per-frame scroll handlers** — never `window.addEventListener('scroll')` in a
  hot path or scroll-driven React state. Use `IntersectionObserver`, CSS
  scroll-driven animations, or a scroll library's batched API.
- **Motion claimed = motion shown.** If the contract sets a lively motion band, the
  page actually moves (entrance, scroll-reveal, hover feedback). If you can't ship
  working motion cleanly, drop the band to static rather than half-build it.

**Responsive, mobile-first.** Design the small screen first, then enhance up.

- Standard breakpoints (`e.g.` 640 / 768 / 1024 / 1280 / 1536). Contain page width
  (`e.g.` `max-w-7xl mx-auto`).
- **Grid over flex-percentage math** for multi-column layouts; declare the mobile
  collapse explicitly per section — no "the framework will handle it."
- **Viewport stability** — use dynamic viewport units for full-height sections
  (`e.g.` `min-h-[100dvh]`), never `100vh`, to avoid mobile address-bar jump.
- Fluid type via a scale or `clamp()`; responsive images with `srcset`/`sizes` and
  lazy-loading below the fold.

## Step 5 — Redesign Protocol

If the surface already exists, classify the mode first:

- **Preserve** — modernize without breaking the brand. Audit first, extract brand
  tokens into the style contract, evolve gradually.
- **Overhaul** — new visual language over existing content and IA. Treat visuals as
  greenfield; preserve content and structure.

Before touching anything, **audit**: brand tokens (color/type/logo/radius),
information architecture, what content is doing real work vs. filler, signature
patterns worth keeping, slop to retire, and the SEO baseline. **Never change
silently:** URL structure, route slugs, primary nav labels, form field names/order
(breaks analytics + autofill), the logo, or legal/consent copy — those need
explicit approval. Apply modernization in risk order: typography → spacing/rhythm →
color recalibration → motion → hero/key-section recomposition → full block
replacement (last resort).

## Relationship to Other Skills

Self-sufficient; the references below are optional and compose only if present.

- **`ux-principles`** (if the project uses it) — decides whether the design *works*:
  hierarchy logic, flows, cognitive load, findability, and the accessibility
  rationale. This skill assumes that layer is sound and makes it *look and feel*
  right. Settle structure and states there; render them here. The AA-contrast and
  reduced-motion invariants are shared.
- **A framework/component skill** (`e.g.` a React or design-system skill, if the
  project uses one) — owns the implementation idioms (component architecture, state,
  RSC boundaries). This skill's contract and invariants ride on top of whatever that
  layer prescribes; where they meet, follow the framework skill for *how* and this
  skill for *how it looks*.

## Pre-Flight Check

Run before delivering. If a box can't be honestly ticked, it isn't done.

- [ ] **Design Read** declared (surface / audience / vibe / style source)
- [ ] **Style contract** resolved from a real source (built-in, described, image, or
      declared inference) — *not* a silent AI default
- [ ] **Locks** held: one theme, one accent, one shape system, one type scale, across
      all sections
- [ ] **Contrast** AA on every button, input, placeholder, focus ring, label
- [ ] **Touch targets** ≥ 44px; keyboard-operable with visible focus
- [ ] **Reduced motion** honored for anything beyond hover/press
- [ ] **Real images** used; zero div-based fake screenshots; real/monogram logos
- [ ] **Zero em-dashes / en-dash separators** anywhere visible
- [ ] **No AI-slop tells** (§3): default aesthetic, decorative filler, "John Doe",
      "Acme", filler verbs, three-equal-cards, eyebrow overuse, zigzag > 2
- [ ] **Every interaction state** present: loading, empty, error, success, disabled
- [ ] **Motion motivated** (one-sentence reason each) and `transform`/`opacity` only;
      no per-frame scroll handlers
- [ ] **Mobile collapse** explicit per section; `min-h-[100dvh]` not `100vh`
- [ ] **Redesign** (if applicable): mode classified, audit done, nothing changed
      silently that breaks brand/SEO/analytics
- [ ] **Enterprise-dense surface?** Deferred to the right official system, not
      hand-rolled
