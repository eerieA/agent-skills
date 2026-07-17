---
name: editorial-warm
summary: A novel, concept-driven style (not a named movement) — the warm, human calm of a well-made printed almanac: sun-warmed paper, ink-and-earth palette, a friendly serif, and unhurried pacing. Approachable and sincere without turning cute.
best_for: wellness & lifestyle, consumer D2C, community & nonprofit, food & recipes, personal brands and newsletters, content-first marketing that wants to feel human
not_for: dense dashboards, data tables, high-urgency/high-stakes tools, hard-tech or enterprise-security briefs wanting a clinical read
mode: light
---

> **This pack is a worked example of the skill's headline claim:** a coherent style
> derived from a *governing concept*, owing nothing to a famous movement. It shows
> the `_template.md` schema and `craft/` reasoning producing a soul with no big name.
> The Voice below deliberately shows the *interpretation* step (`craft/stylization.md`)
> rather than a category lookup.

## 1. Voice / Governing Concept

**Governing concept: a well-thumbed printed almanac left on a sunny kitchen table.**
Not "friendly consumer app" (that's the lookup, and it lands as rounded-blue-blob
slop). The interpreted reading: the audience wants to feel *looked after by
something made with care* — the warmth of a reference book someone has kept for
years, with soft paper, warm ink, and a calm, generous hand. Every token descends
from that: warmth over brightness, paper over screen-white, a reading serif over a
neutral sans, unhurried pacing over snappy energy.

The through-line is **sincerity through craft, not decoration**. Warmth comes from
material and restraint (paper tone, earthy ink, room to breathe), *not* from emoji,
rainbow gradients, or bouncy mascots — those are the cheap shortcuts to "friendly"
that read as insincere. This style is soft but never saccharine, human but never
juvenile. Rejects: cold clinical minimalism, saturated tech gloss, playful-blob
consumer defaults, and anything that mistakes brightness for warmth.

## 2. Palette

Warm, low-contrast-but-accessible, ink-and-earth. The warmth lives in the neutrals,
not in a loud accent.

- **Background** — sun-warmed paper: `#FAF6EF` / `#F6F0E4` (warm cream, never
  screen-white `#FFF`).
- **Surface** — a half-step warmer/lighter panel `#FFFDF8` or a soft `#F1E9DA`.
- **Borders / dividers** — warm low-contrast `#E4D9C6` / `rgba(60,40,20,0.10)`.
- **Text** — warm near-black espresso `#2B2420` (never pure `#000`); secondary
  muted clay `#6F6357`.
- **Accent (one, earthy)** — a warm analogous accent: terracotta `#C4643C` *or*
  ochre `#C08A2E` *or* sage `#6E7F5B` — pick ONE and hold. Used for links, the
  primary CTA, and small emphasis; warm and grounded, never neon.
- **Support hue (optional, analogous)** — one adjacent earthy tone for tags/
  illustration only (`e.g.` sage alongside terracotta), never a second CTA color.
- **Semantic states** — muted and earth-consistent: brick-red error, amber caution,
  moss success — desaturated to sit in the palette, still AA.
- **Contrast:** warm palettes tempt low-contrast text. Espresso `#2B2420` on cream
  clears AA comfortably; verify the accent-on-cream CTA and muted secondary text.
  The AA floor overrides any cozy-looking pairing.

## 3. Typography

- **Display / headline** — a warm reading **serif** with a little character
  (`e.g.` a humanist/old-style or a soft slab), moderate size, normal-to-slightly-
  loose leading. The serif is the primary carrier of the "made by a person" feeling.
- **Body** — a comfortable humanist serif *or* a warm humanist sans (not a cold
  grotesk, not Inter/Roboto default). Reading-optimized: ~60–70ch line length,
  line-height ~1.6, `≥16px` mobile.
- **Mono** — sparing, for a recipe measurement / metadata / a wink of the "field
  notes" texture; optional.
- **Emphasis** — same-family italic (a real italic, which warm serifs do well) or
  weight; the italic serif is a signature emphasis here.
- **Scale** — gentle ratio (1.2×). Contrast is *moderate*, not dramatic — the calm
  pacing is part of the concept; extreme scale jumps would read as urgent, off-tone.

## 4. Shape

- **Corner radius** — soft but modest: `8–12px` on cards, `6–8px` on buttons.
  Gently rounded, evoking a worn paper edge — *not* `rounded-full` blobs (that's the
  consumer-default cliché the concept rejects). One radius system, held.
- **Borders / dividers** — thin warm `1px` rules; a soft divider or a subtle warm
  panel replaces a hard card wherever elevation isn't doing real work.

## 5. Density and Layout

- **Grid**
  - **Philosophy** — a calm, mostly **symmetric editorial grid** (single generous
    column for reading, simple 2–3 up for cards). Orderly and unhurried, like a
    book page; not the bento asymmetry of minimalist, not the rigid matrix of
    brutalist.
  - **Visibility** — grid is *hidden*: felt through consistent margins and a steady
    baseline rhythm, not drawn. Structure reads as tidiness, not as lines.
  - **Grid-breaks** — occasional and warm: a full-bleed photograph, or a pull-quote
    that steps into the margin like a marginal note. Breaks feel like a personal
    annotation, never a jolt.
  - *Column/gutter mechanics per surface (Step 4).*
- **Spacing** — generous and even; unhurried vertical rhythm (`e.g.` `py-20`–`py-28`
  sections). Room to breathe is where the calm comes from.
- **Content width** — reading-first: primary text `max-w-2xl`–`max-w-3xl`, centered
  or left on a comfortable measure.

## 6. Elevation

Hierarchy from **warm type, space, and a single earthy accent**, not depth. Shadows,
if any, are warm-tinted and very soft (`e.g.` `0 4px 16px rgba(80,50,20,0.06)`) —
tinted to the paper, never a cold grey/black drop. Prefer grouping by warm panels,
soft dividers, and space over drawn cards.

## 7. Motion

- **Intensity band** — subtle and gentle; motion should feel *calm and settling*,
  like turning a page, never energetic.
- **Signature** — soft fades with a small rise (`translateY(8px)` + `opacity`),
  ~450ms, ease-out (`cubic-bezier(0.16,1,0.3,1)`), via `IntersectionObserver`.
  Gentle staggered reveals for lists. Buttons settle with a small `scale(0.98)` press.
- **Never** — bouncy spring, snappy fast micro-motion, playful wobble (all read as
  juvenile and break the sincere-calm tone). Honor `prefers-reduced-motion`: collapse
  to static.

## 8. Imagery and Icons

- **Photography** — warm, natural-light, lived-in; gentle warm grade, real texture
  (hands, paper, food, place). A whisper of warm grain (`~0.03`) to sit in the paper
  tone. Never cold, oversaturated, or stocky-perfect.
- **Illustration** — warm hand-drawn or textured line/spot illustration in the
  accent + support hue; a small "field-guide sketch" quality reinforces the concept.
- **Icons** — a single humanist line family with slightly rounded joins (warm, not
  clinical), standardized stroke, in espresso or the accent.
- **Banned** — emoji as decoration; rainbow/neon gradients; glassmorphism; cold blue
  tech imagery; playful 3D blobs; more than one accent shouting for attention.

## 9. Signature Moves and Anti-Patterns

**Signature moves**
- Warm cream paper ground with espresso ink and one earthy accent.
- A characterful reading serif headline; italic-serif for emphasis.
- Pull-quotes / captions set like marginal notes stepping into the margin.
- Warm natural-light photography with a whisper of grain.
- Unhurried vertical rhythm; a single earthy CTA that feels grounded, not loud.

**Anti-patterns (override these)**
- `rounded-full` blob cards + bright blue + emoji (the "friendly app" lookup this
  concept explicitly rejects).
- Screen-white `#FFF` backgrounds; cold grey neutrals; Inter/Roboto default.
- Two competing accents; neon/rainbow; saturated tech gradients; glassmorphism.
- Dramatic scale contrast or snappy/bouncy motion (reads urgent or juvenile — wrong
  tone).
- Warmth faked with color temperature filters over cold stock instead of genuinely
  warm, lived-in imagery.
- "John Doe" / "Acme" / "Lorem Ipsum"; AI filler verbs; cutesy microcopy.
