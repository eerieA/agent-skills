# Style Contract Template

A **style pack** fills in this schema to give the `ui-taste` skill a concrete
aesthetic. The skill's *invariants* (WCAG contrast, touch targets, reduced motion,
the consistency locks, image/logo honesty) always apply on top — a style pack sets
values *within* those constraints and may never relax them.

Use this file three ways:
1. **Author a new built-in** — copy it to `styles/<name>.md`, fill every section,
   commit it. It becomes selectable by name.
2. **Capture a described style** — when the user describes a look in text, fill this
   schema from their words and echo it back for confirmation before building.
3. **Capture a reference image / site** — extract the tokens below from the
   reference and echo them back so the user can correct the reading.

Keep each section concrete. A style pack is only useful if it makes decisions the
skill would otherwise default on. Vague packs ("clean and modern") produce slop.

---

## Frontmatter

```yaml
---
name: <style-slug>           # e.g. minimalist, brutalist, editorial-warm
summary: <one line>          # what this style is, in a sentence
best_for: <surface list>     # e.g. landing pages, portfolios, dashboards
not_for: <surface list>      # where this style actively hurts
mode: light | dark | both    # which theme(s) this style commits to
---
```

## 1. Voice / Governing Concept (one paragraph)

State the **governing concept** first — the one idea this style is built on (a
metaphor, material, mood, or tension). Then: what is it *trying to feel like*, and
what does it deliberately reject? Name reference points (movements, products, print
traditions) as *devices to remix*, not looks to imitate. Every token below must be
traceable back to this concept; anything that doesn't serve it is cut. This
paragraph is the soul of the style and the tie-breaker when a lower-level rule is
silent. See `craft/stylization.md` for how to derive and commit to a concept
(including the interpretation-not-lookup test).

## 2. Palette

- **Neutrals** — 4–5 steps from background to primary text. Off-black and off-white
  only; never pure `#000` / `#fff`. Warm or cool, chosen intentionally and held.
- **Accent** — at most one. Its hex, and the rule for when it may appear.
- **Semantic states** — success / warning / error / info, if the surface needs them.
- **Light and dark values** — if `mode: both`, give both. Maintain hierarchy parity
  and AA contrast across modes; keep the brand accent recognizable in both.

## 3. Typography

- **Display / headline face** — the face (or category), plus tracking and leading
  rules at large sizes.
- **Body face** — optimized for reading; line length target (`~45–75ch`), line
  height, size floor (`≥16px` on mobile to avoid zoom).
- **Mono face** — if the style uses one, and for what (code, metadata, keystrokes).
- **Scale** — a ratio-based scale (`e.g.` 1.25×), or `clamp()` ranges for fluid type.
- **Emphasis rule** — how to emphasize within a headline (same-family italic/bold,
  never a random second family).

## 4. Shape

- **Corner radius** — the single system (all-sharp `0`, all-soft, all-pill), or the
  documented mixed rule and where each radius applies.
- **Borders / dividers** — weight, color (from the neutral steps), when a border
  replaces a card.

## 5. Density and Layout

- **Spacing scale** — the base unit and section rhythm (airy vs. packed).
- **Content width** — max reading/content width.
- **Grid** — the *stylistic* grid traits (not the per-surface mechanics):
  - **Philosophy** — strict/columnar, modular, asymmetric, broken, or spontaneous.
    A style's grid discipline is a real personality signal: a rigid columnar grid
    reads ordered and trustworthy; a broken or off-axis grid reads dynamic and
    editorial. Pick one on purpose and hold it.
  - **Visibility** — does this style *show* its grid (visible alignment, rules, or
    column seams as an aesthetic, à la Swiss) or hide it (grid felt through
    alignment only)? Showing vs. hiding is itself a stylistic choice.
  - **Grid-breaks** — how much this style invites deliberate breaks (a bleed, a
    span, one off-axis element as a focal point) versus keeping every element on the
    grid. State the rule so breaks read as intentional, not accidental.
  - *Column counts, gutters, margins, and breakpoints are per-surface mechanics —
    they live in the skill's responsive step (Step 4), not here. How to reason about
    grid as composition is in `craft/composition.md`.*

## 6. Elevation

How hierarchy is expressed: shadow, border, background shift, or pure spacing. If
shadows are used, their tint and opacity ceiling. Many styles express hierarchy
*without* shadow — state that if so.

## 7. Motion

- **Intensity band** — static / subtle / fluid / choreographed.
- **Default easing + durations** — the style's signature curve and timing (within
  the skill's global timing guidance).
- **What may move, and why** — the motivated-motion rule, specialized to this style.
  What this style specifically must *not* do (`e.g.` "no bouncy spring; motion is
  invisible").

## 8. Imagery and Icons

- **Photography / illustration treatment** — filters, tone, overlays, or "none."
- **Icon family + weight** — one family, standardized stroke.
- **What's banned** — `e.g.` emoji, stock-photo saturation, gradient blobs.

## 9. Signature Moves and Anti-Patterns

- **Signature moves** — 3–6 concrete devices that make this style recognizable.
- **Anti-patterns** — the specific ways this style is most often done *wrong*,
  including the generic defaults it must override.

---

**Reminder:** the pack configures knobs; the skill enforces guardrails. If any
value here would violate an invariant (contrast, targets, reduced-motion, honesty),
the invariant wins and the pack value is clamped.
