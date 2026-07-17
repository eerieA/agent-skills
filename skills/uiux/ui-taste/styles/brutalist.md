---
name: brutalist
summary: Raw industrial brutalism — mid-century Swiss print fused with tactical/aerospace terminal aesthetics. Rigid grids, extreme type-scale contrast, utilitarian color, analog degradation. Pick ONE of two substrate modes and commit.
best_for: data-heavy dashboards, portfolios, editorial sites, launch pages that want to feel like declassified blueprints or industrial manuals
not_for: trust-first / consumer-warm / accessibility-critical-soft briefs, kids' products, anything wanting approachable friendliness
mode: both
---

## 1. Voice

Digital environments that project raw functionality, mechanical precision, and
high data density, deliberately discarding consumer-UI softness. Two compatible
paradigms — **pick ONE per project and commit; never alternate or mix both within
one interface:**

- **Swiss Industrial Print (light)** — 1960s corporate identity + heavy-machinery
  blueprints. High-contrast light substrate, monolithic heavy sans, visible grid
  dividing lines, aggressive asymmetric negative space punctuated by oversized
  viewport-bleeding numerals, hazard red as the single accent.
- **Tactical Telemetry / CRT Terminal (dark)** — classified databases, legacy
  mainframes, aerospace HUDs. Dark substrate, dense tabular data, dominant
  monospace, ASCII framing devices, simulated hardware limits (phosphor glow,
  scanlines, low bit-depth).

Typography and grid carry the design; imagery is secondary and always degraded.

## 2. Palette

Uncompromising. **Gradients, soft shadows, and modern translucency are prohibited.**
Colors simulate physical media or primitive emissive displays. Choose ONE substrate
and hold it — never mix light and dark substrates in one interface.

**Swiss Industrial Print (light)**
- **Background** — `#F4F4F0` or `#EAE8E3` (unbleached documentation paper).
- **Foreground** — `#050505`–`#111111` (carbon ink).
- **Accent** — `#E61919` / `#FF2A2A` (aviation/hazard red). The *only* accent —
  strike-throughs, thick structural dividers, vital-data highlights.

**Tactical Telemetry (dark)**
- **Background** — `#0A0A0A` or `#121212` (deactivated CRT; never pure `#000`).
- **Foreground** — `#EAEAEA` (white phosphor), the primary text color.
- **Accent** — same hazard red, same rules.
- **Terminal green** `#4AF626` — optional, for exactly one purposeful element
  (a single status readout); never a general text color. Omit if it has no job.

> Contrast note: hazard red on paper/CRT can fail AA for small text. Use red for
> large text, rules, and highlights — not body copy. The skill's AA floor still applies.

## 3. Typography

- **Macro (structural headers)** — neo-grotesque / heavy sans (`e.g.` Neue Haas
  Grotesk Black, Archivo Black, Inter Black, Monument Extended). Massive fluid scale
  (`clamp(4rem, 10vw, 15rem)`), very tight tracking (`-0.03em` to `-0.06em`),
  compressed leading (`0.85`–`0.95`), **uppercase**.
- **Micro (data / telemetry)** — monospace (`e.g.` JetBrains Mono, IBM Plex Mono,
  Space Mono). Fixed small (`10–14px`), generous tracking (`0.05–0.1em`), uppercase;
  used for all metadata, nav, IDs, coordinates.
- **Textural disruption** — a high-contrast serif (`e.g.` Playfair, EB Garamond),
  used *exceedingly* sparingly and always heavily degraded (halftone / 1-bit dither).
- **Scale** — extreme variance between macro and micro is the whole point.

## 4. Shape

- **Corner radius** — **`0` everywhere.** All corners exactly 90°. Radius is banned;
  it reads as soft/consumer and breaks the mechanical rigidity.
- **Borders** — solid `1px`/`2px` rules delineate every zone; `<hr>` spans full
  container width to segregate units. Razor-thin dividers via `display:grid;
  gap:1px` over a contrasting parent background.

## 5. Density and Layout

- **Grid**
  - **Philosophy** — the *blueprint grid*: strict, rigid CSS Grid; elements anchor
    to tracks and intersections and never float. The grid is the skeleton, not a
    suggestion. This rigidity is core to the mechanical character.
  - **Visibility** — grid is emphatically *shown*: bordered zones, full-width
    horizontal rules, crosshairs (`+`) at intersections, `gap:1px` dividing lines.
    The visible structure is the aesthetic — the viewer should read the grid as a
    diagram.
  - **Grid-breaks** — the one sanctioned break is the oversized viewport-bleeding
    numeral/letterform that punches out of the tracks as a focal point. That bleed
    is deliberate and reads *against* the rigid grid; everything else stays locked.
    No casual off-axis drift.
- **Bimodal density** — oscillate between extreme data density (tight monospace
  clusters) and vast calculated negative space framing macro-type. This tension is
  the signature.
- **Content width** — full-bleed structural elements; data blocks can run edge to edge.

## 6. Elevation

None in the modern sense. **No shadows, no depth blur, no translucency.** Hierarchy
is pure: type scale, border weight, grid position, and the red accent. Layering is
flat and diagrammatic.

## 7. Motion

- **Intensity band** — mechanical/minimal. Motion simulates machinery, not delight.
- **Signature** — sharp snap easing (`cubic-bezier(0.4,0,0.6,1)`), terminal-style
  reveals (type-on, scanline sweep), randomized "active process" data strings
  (`REV 2.6`, `UNIT / D-01`). No smooth organic curves; no bounce.
- **Never** — bouncy spring, playful float, decorative parallax. Honor
  `prefers-reduced-motion`: scanlines/flicker/glow collapse to static.

## 8. Imagery and Icons

- **Photography** — always degraded: halftone or 1-bit dithering, `mix-blend-mode:
  multiply` over SVG dot patterns. No clean full-color photography.
- **Textural effects** — CRT scanlines (`repeating-linear-gradient`), a global
  low-opacity SVG noise/grain on the DOM root, halftone on large serif type.
- **Symbology over icons** — ASCII framing (`[ DELIVERY SYSTEMS ]`, `>>>`, `///`),
  crosshairs (`+`) at grid intersections, barcode rules, thick warning stripes,
  `®`/`©`/`™` used as structural geometric marks (not legal text). Standard icon
  libraries are secondary; when used, sharp/technical weights only.
- **Semantic HTML** — build telemetry with `<data>`, `<samp>`, `<kbd>`, `<output>`,
  `<dl>` to match the technical character.

## 9. Signature Moves and Anti-Patterns

**Signature moves**
- Oversized viewport-bleeding uppercase numeral/letterform as hero.
- `gap:1px` grid producing razor dividing lines without border spam.
- ASCII-bracketed section labels; crosshairs at intersections; barcode strips.
- Full-width `<hr>` unit separators; monospace metadata clusters.
- One (and only one) hazard-red highlight per view; scanline/grain texture layer.

**Anti-patterns (override these)**
- Any `border-radius`; drop shadows; gradients; glassmorphism; translucency.
- Mixing the light and dark substrates in one interface.
- Terminal green used as general text (it's a single-element accent or omitted).
- Clean undegraded photography; soft pastel palettes; friendly rounded consumer UI.
- Red body text that fails AA (keep red to large text, rules, highlights).
