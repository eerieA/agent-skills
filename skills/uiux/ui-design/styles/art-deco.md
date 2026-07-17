---
name: art-deco
summary: Machine-age glamour — geometric ornament, strict symmetry, deep jewel tones with restrained metallic accent, and tall vertical emphasis. Luxury as engineered composition, not decoration for its own sake.
best_for: luxury brands, hospitality/hotels, spirits & fragrance, events & galas, film/theatre, premium editorial, awards and anniversary pages
not_for: dense dashboards, data tables, utilitarian tools, accessibility-critical-soft or kids' products, anything wanting casual friendliness
mode: dark
---

## 1. Voice / Governing Concept

**Governing concept: a 1920s grand-hotel lobby rendered in metal and stone.**
Everything descends from that image — the surface should feel like polished
architecture: symmetrical, vertical, ceremonial, expensive. Art Deco's soul is
*ornament that obeys geometry*: the decoration is real (sunbursts, chevrons,
stepped forms, fluting) but it is always built from disciplined geometric units and
laid out with strict symmetry, never freehand flourish. That discipline is what
separates Deco glamour from gaudy pastiche.

Remix the movement's *devices*, don't cosplay the era: pull Deco's symmetry +
geometric ornament + metallic-on-dark contrast + vertical emphasis, and drop the
literal period kitsch (gold everything, gatsby fonts, champagne-glass clip art).
The result should read as *timeless luxury with a machine-age spine*, not a themed
party. Rejects: flat minimalism's emptiness, organic softness, playful asymmetry,
gradient/glass modern gloss.

## 2. Palette

Deep, saturated, and dark-grounded, with metal as the single precious accent.

- **Background** — deep near-black with a hue: ink `#0E0E12`, or a jewel-dark like
  midnight teal `#0C1B1E` / oxblood `#1A0E10` (never pure `#000`). Pick one and hold.
- **Surface** — a half-step lift of the background (`#16161C` class), or a panel in
  a second jewel tone.
- **Jewel field colors** — one or two deep saturated tones for large fields:
  emerald `#0F5C4A`, sapphire `#173A6B`, garnet `#6E1423`, aubergine `#3A2150`.
  Rich, not neon.
- **Metallic accent (the one precious color)** — warm brass/champagne-gold
  `#C6A15B` / `#D8B978`, *or* cool platinum `#C9CDD3` — choose ONE metal and keep it.
  Used for hairlines, rules, ornament linework, key type, and the primary CTA edge.
  Metal is scarce and always reads as the most valuable ink on the page.
- **Text** — warm off-white `#F2EEE6` on dark; secondary muted `#B7B1A4`.
- **Semantic states** — kept muted and jewel-consistent (deep red for error, etc.)
  so they don't compete with the metallic accent.
- **Contrast note:** brass/gold on jewel fields can fail AA at body sizes. Use the
  metallic for **large type, rules, and ornament** — not paragraph text; body copy
  is the off-white. The skill's AA floor overrides any glamour choice.

## 3. Typography

- **Display / headline** — high-contrast geometric or fashion-serif with strong
  thick/thin modulation (`e.g.` a Deco-geometric caps face, or a high-contrast
  didone). **Uppercase**, letter-spaced (`0.05–0.15em`), often stacked in a tall
  narrow column. This is the ornamental voice.
- **Body / UI** — a clean humanist or geometric sans for readability; keep it quiet
  so the display face carries the drama. `≥16px` mobile, line length ~60–70ch.
- **Emphasis** — within the same family (weight/italic) or via letter-spacing and
  the metallic color; never a random third face.
- **Scale** — dramatic contrast between a tall letter-spaced display and calm body;
  the vertical, ceremonial headline is the signature.

## 4. Shape

- **Corner radius** — sharp `0`, or a *documented stepped/chamfered* corner
  (a small 45° cut or a two-step ziggurat corner) applied consistently. No soft
  rounding — Deco corners are engineered, not friendly.
- **Borders / dividers** — thin metallic hairlines (`1px`), often doubled (a thin +
  thicker pair) as a Deco framing device. Symmetrical frames around key blocks.

## 5. Density and Layout

- **Grid**
  - **Philosophy** — strict and **symmetric**, with pronounced **vertical
    emphasis**: centered axes, mirrored compositions, tall columns. Symmetry is a
    core personality signal here (unlike brutalist's asymmetry or minimalist's bento).
  - **Visibility** — grid is *shown through framing*: metallic rules, symmetric
    borders, and ornamental dividers make the structure visible as decoration.
    Alignment reads as deliberate architecture.
  - **Grid-breaks** — rare and centered: a single oversized ornamental motif
    (sunburst, stepped arch) on the central axis may anchor a hero. Breaks respect
    symmetry — no off-axis drift; the axis is sacred.
  - *Column/gutter mechanics per surface (Step 4).*
- **Spacing** — generous and ceremonial; large vertical rhythm frames the content
  like a proscenium. Airy, not packed.
- **Content width** — contained and centered; primary text `max-w-3xl`–`max-w-4xl`
  on a centered axis.

## 6. Elevation

Hierarchy comes from **metallic contrast, symmetric framing, and scale**, not soft
shadow. Depth is expressed by layered frames and rule-work (a framed panel inside a
framed section), diagrammatic and flat. If any shadow is used, keep it a crisp
low-opacity edge, never a soft modern blur. No glassmorphism, no gradient glow.

## 7. Motion

- **Intensity band** — subtle and elegant; motion should feel *choreographed and
  deliberate*, like a curtain or a mechanism, never bouncy.
- **Signature** — symmetric reveals (elements resolve from the center axis outward,
  or a metallic rule draws in horizontally then content fades up); slow, precise
  easing (`cubic-bezier(0.22, 1, 0.36, 1)`), ~500ms. An ornamental motif may draw
  its linework on once on entry.
- **Never** — spring bounce, playful float, fast micro-jitter. Honor
  `prefers-reduced-motion`: line-draws and reveals collapse to static.

## 8. Imagery and Icons

- **Photography** — rich, moody, warm-lit; high-end editorial tone. May carry a
  subtle metallic-duotone or a thin metallic frame. No flat bright stock.
- **Ornament** — geometric Deco motifs as SVG linework in the metallic accent:
  sunbursts, chevrons, stepped/ziggurat forms, fluting, symmetric borders. Ornament
  is *linear and geometric*, used at focal points, never scattered as filler.
- **Icons** — a thin geometric line family in the metallic accent, standardized
  stroke; sharp joins, no rounded caps.
- **Banned** — emoji; literal gatsby/champagne clip art; gold gradients and bevels;
  drop-shadow "3D gold"; more than one metal; ornament used as background wallpaper.

## 9. Signature Moves and Anti-Patterns

**Signature moves**
- Tall, letter-spaced uppercase display on a centered vertical axis.
- One metallic accent for hairlines, doubled framing rules, and key type.
- A single geometric ornament (sunburst / stepped arch) anchoring the hero on-axis.
- Symmetric framed panels; content reveals from the center outward.
- Jewel-dark ground with off-white body and scarce, precious metal.

**Anti-patterns (override these)**
- Gold *everything*; two competing metals; gradient/bevel "shiny gold" effects.
- Period-kitsch fonts or champagne/gatsby clip art (cosplay, not design).
- Asymmetric or broken layouts (that's a different soul); off-axis focal points.
- Soft rounding, glassmorphism, gradient glow, modern SaaS gloss.
- Metallic body text that fails AA (keep metal to large type, rules, ornament).
- "John Doe" / "Acme" / "Lorem Ipsum"; AI filler verbs.
