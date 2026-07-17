---
name: minimalist
summary: Warm monochrome, editorial "document-style" minimalism — typographic contrast and whitespace carry the design; near-zero shadow, no gradients.
best_for: landing pages, portfolios, editorial/blog, docs, calm SaaS marketing, content-first product screens
not_for: high-density dashboards, data-heavy tables, anything needing loud saturated color as a functional signal
mode: both
---

## 1. Voice

Premium utilitarian minimalism in the lineage of top-tier workspace tools and
editorial print. The page should read like a well-set document: quiet, confident,
uncluttered, with hierarchy carried by type and space rather than color or
ornament. It rejects generic SaaS gloss — no drop-shadow depth, no gradient hero
blobs, no glassmorphism. Restraint is the point; every element must earn its place.
Minimalism is *not* emptiness: sections still get subtle depth (low-opacity
imagery, a faint warm radial, a thin pattern) so they don't read as flat or unfinished.

## 2. Palette

- **Canvas / background** — pure white `#FFFFFF` or warm bone `#F7F6F3` / `#FBFBFA`.
- **Surface (cards)** — `#FFFFFF` or `#F9F9F8`.
- **Borders / dividers** — ultra-light `#EAEAEA` or `rgba(0,0,0,0.06)`.
- **Text** — off-black charcoal `#111111` or `#2F3437` (never pure `#000`), body
  line-height ~1.6; secondary text muted `#787774`.
- **Accent** — color is scarce; used only for semantic meaning or subtle tags. Use
  highly desaturated washed pastels, each with an accessible text pairing:
  pale red `#FDEBEC` (text `#9F2F2D`), pale blue `#E1F3FE` (text `#1F6C9F`), pale
  green `#EDF3EC` (text `#346538`), pale yellow `#FBF3DB` (text `#956400`).
- **Dark mode** — warm near-black canvas (not pure black), off-white text, borders
  at low white opacity; keep the same restraint and AA contrast.

## 3. Typography

- **Display / headline** — clean geometric or editorial serif, tight tracking
  (`-0.02em` to `-0.04em`) and tight leading (~1.1). `e.g.` a refined grotesk for
  a modern read, or an editorial serif (`e.g.` Newsreader-class) for a literary one.
  Commit to one direction per project.
- **Body / UI** — a clean humanist or geometric sans with character; **not** Inter/
  Roboto/Open Sans as a default. Line length ~60–70ch, `≥16px` on mobile.
- **Mono** — for metadata, code, keystrokes (`<kbd>`), and small technical labels.
- **Scale** — ratio-based (1.2–1.25×). Extreme *contrast* between display and body
  sizes is the editorial signature.

## 4. Shape

- **Corner radius** — crisp and small: `8px` or `12px` max on cards; `4–6px` on
  buttons. **No `rounded-full`** on large containers or primary buttons (pills are
  allowed only for small tags/badges).
- **Borders** — exactly `1px solid #EAEAEA` on cards, dividers, and `<kbd>` keys.
  A border/divider replaces a card whenever elevation isn't communicating hierarchy.

## 5. Density and Layout

- **Spacing** — generous macro-whitespace; large vertical section padding
  (`e.g.` `py-24`–`py-32`). Establish the whitespace rhythm *first*.
- **Content width** — constrain primary text to `max-w-4xl`–`max-w-5xl`.
- **Grid**
  - **Philosophy** — asymmetric and modular (bento grids with mixed cell sizes),
    never a rigid uniform matrix. Moderate layout variance — calm, not chaotic.
  - **Visibility** — grid is *hidden*: felt through alignment and consistent
    whitespace, never shown as visible rules or column seams. Order comes from
    breathing room, not drawn structure.
  - **Grid-breaks** — sparing. An occasional full-bleed image or a single oversized
    editorial pull-quote may break the column; otherwise everything aligns quietly.
    A break should feel like a considered emphasis, not a disruption.
  - *Card padding stays generous (`24–40px`); column/gutter mechanics per surface
    (Step 4).*

## 6. Elevation

Hierarchy comes from **type scale, contrast, and space**, not depth. Shadows are
practically non-existent: if used at all, ultra-diffuse and `< 0.05` opacity
(`e.g.` a card hover lifting to `0 2px 8px rgba(0,0,0,0.04)`). No heavy
`shadow-md/lg/xl`.

## 7. Motion

- **Intensity band** — subtle. Motion should be felt, not seen.
- **Signature** — gentle scroll-entry fades: `translateY(12px)` + `opacity:0`
  resolving over ~600ms with `cubic-bezier(0.16, 1, 0.3, 1)`, via
  `IntersectionObserver`. Staggered list/grid reveals (`~80ms` cascade). Buttons
  `scale(0.98)` on `:active`.
- **Ambient** — optional single very-slow radial-gradient drift behind a hero
  (`20s+`, opacity `0.02–0.04`), on a `fixed; pointer-events:none` layer only.
- **Never** — bouncy spring, attention-grabbing loops, motion on scrolling
  containers. Honor `prefers-reduced-motion` (collapse to static).

## 8. Imagery and Icons

- **Photography** — high-quality, desaturated, warm-toned; subtle low-opacity grain
  overlay (`~0.04`) to blend into the monochrome. Never oversaturated stock.
- **Illustration** — monochrome continuous-line ink sketches with a single offset
  muted-pastel shape.
- **Section backgrounds** — add quiet depth (low-opacity full-width imagery, a soft
  warm radial `~0.03`, or a minimal line pattern); sections must not read as flat.
- **Icons** — Phosphor (Bold/Fill) or Radix, standardized stroke, slightly thicker
  for a technical-editorial feel. No thin generic line sets as default.
- **Banned** — emoji anywhere; gradient blobs; glassmorphism beyond a subtle nav blur.

## 9. Signature Moves and Anti-Patterns

**Signature moves**
- Bento feature grid, `1px` borders, crisp small radius, generous padding.
- Faux-OS window chrome (white top bar, three light-grey dots) when mocking software.
- `<kbd>` keystroke keys in mono for shortcuts.
- FAQ accordions stripped to a single `border-bottom` divider with a sharp `+`/`-`.
- Solid `#111` CTA button, white text, `4–6px` radius, no shadow.

**Anti-patterns (override these)**
- Inter/Roboto/Open Sans; heavy Tailwind shadows; primary-colored hero sections;
  gradients / neon / 3D glass; `rounded-full` big containers; emoji; "John Doe" /
  "Acme" / "Lorem Ipsum"; AI filler verbs.
- **Pure-text "minimalism"** — a page with no images is not minimal, it's
  unfinished. Even a restrained site needs a few real (B&W/desaturated) images.
