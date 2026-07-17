# references — ui-taste

Author-only memory-jog for what this skill (and its style packs) were built on.
Not part of the skill; leave out when copying the skill into a project.

## Sources

- **`taste-skill` / `design-taste-frontend` SKILL.md** (Leonxlnx/taste-skill)
  (https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill)
  — the primary backbone. Source of the whole anti-slop spine: brief-read /
  Design-Read, the anti-default discipline, the brief→design-system map (defer dense
  UI to official systems), the AI-tells catalog, the em-dash ban, the consistency
  locks (theme/color/shape), interaction-state requirements, motion-must-be-motivated,
  the redesign protocol, and the pre-flight check. Adapted, not copied: its
  React/Next/Tailwind/Motion defaults and 3-dials mechanism were generalized — the
  dials became the normalized **style contract** (palette/type/shape/density/motion/
  elevation) and the framework specifics were demoted to clearly-labeled `e.g.`
  illustrations so the skill stays stack-agnostic. Its scope was widened from
  "landing/portfolio only" to general product + marketing UI per the direction chosen.

- **`bencium-controlled-ux-designer` SKILL.md + MOTION-SPEC.md + RESPONSIVE-DESIGN.md**
  (bencium-marketplace)
  (https://github.com/bencium/bencium-marketplace/blob/main/bencium-controlled-ux-designer/skills/bencium-controlled-ux-designer/)
  — source of the visual-craft layer: material honesty (affordance via color/spacing,
  not shadow), functional layering over skeuomorphic depth, the motion timing tables
  and easing curves (Step 4), and the mobile-first responsive discipline (breakpoints,
  grid-over-flex-math, viewport stability, fluid type, responsive images). Adapted:
  condensed the two companion files into Step 4 principles + `e.g.` snippets; its
  UX-principle content (hierarchy, feedback, forgiveness, progressive disclosure)
  was routed to `ux-principles` to keep the UX/UI split clean.

## Craft references (`craft/`) — the aesthetic-reasoning layer

Added to give the skill a *generative* half. The original skill was strong at
anti-slop discipline (what not to do) but thin on how to reason about visual
aesthetics (what makes a surface actually good and personal). These on-demand files
are consulted from **Step 1.5**; they sit below the invariants and never override
them.

- **`craft/stylization.md`** ← **"11 Key Graphic Design Styles"** (Looka)
  (https://looka.com/blog/graphic-design-styles/) + **"Graphic Design"** (Interaction
  Design Foundation) (https://ixdf.org/literature/topics/graphic-design). The headline
  addition. Sources of: the **governing concept** as the seat of personality;
  **interpretation-not-lookup** as where the "human touch" comes from (added per the
  user's point that a designer's reading is filtered through lived experience — the
  operationalized version is "refuse the generic reading, commit to a defensible
  specific one; two designers should reach two valid souls"); the **movements-as-
  devices-to-remix** table (Swiss/Bauhaus/Art Deco/Pop/Psychedelic/Postmodern/
  Brutalism/Flat/Contemporary → devices → feeling); design-is-emotional + Maeda's
  "design solves a problem, art asks one." Deliberately framed so personality
  *reinforces* the consistency locks (commit-to-one-premise) rather than fighting
  them.

- **`craft/color.md`** ← **"Color combinations"** (Figma resource library)
  (https://www.figma.com/resource-library/color-combinations/).
  Source of: harmony types (mono/analogous/complementary/split/triadic/tetradic);
  color properties (hue/value/saturation/temperature) as the tuning knobs that do
  the hierarchy + mood work; a color-psychology table; the concept→harmony→neutrals→
  accent build method. Reconciled with the skill's existing one-accent lock (harmony
  ≠ many competing CTAs) and clamped under the AA floor.

- **`craft/composition.md`** ← **"Golden Rules of Composition"** (MakeUseOf)
  (https://www.makeuseof.com/graphic-design-rules-of-composition/) + **"Visual
  Hierarchy in UX: Definition"** (Nielsen Norman Group)
  (https://www.nngroup.com/articles/visual-hierarchy-ux-definition/). Source of:
  grid, focal point, layering,
  texture, negative space, and — per the user's framing — **hierarchy as aesthetic
  rhythm**, not only information architecture (the intervals between sizes/contrast/
  space create a cadence). Includes the **squint test** from the NN/g piece. The
  golden-rules article's "these aren't golden, learn-then-break" stance is honored:
  grid-break / rule-break framed as deliberate, concept-serving moves.

## Style packs

- **`minimalist.md`** ← **`minimalist-skill` / `minimalist-ui`** (Leonxlnx/taste-skill)
  (https://github.com/Leonxlnx/taste-skill/blob/main/skills/minimalist-skill/)
  — the warm-monochrome editorial minimalism spec (palette, 1px borders, crisp small
  radius, generous whitespace, subtle scroll-entry motion, degraded imagery, faux-OS
  chrome, `<kbd>` keys). Reshaped into the style-contract schema.

- **`brutalist.md`** ← **`brutalist-skill` / `industrial-brutalist-ui`** (Leonxlnx/taste-skill)
  (https://github.com/Leonxlnx/taste-skill/blob/main/skills/brutalist-skill/)
  — the Swiss-industrial-vs-tactical-terminal spec (dual substrate, heavy-sans +
  monospace type architecture, hazard-red single accent, `0` radius, blueprint grid,
  analog degradation / scanlines / halftone, ASCII symbology). Reshaped into the
  style-contract schema; added the AA note about red-on-substrate contrast.

- **`art-deco.md`** — authored as a worked example of the enriched template
  (governing concept in Voice + the new Grid sub-section). Movement devices drawn
  from `craft/stylization.md`'s Art Deco row (symmetry, geometric ornament, metallic
  + jewel tones, vertical emphasis), remixed rather than period-cosplayed. Chosen to
  exercise the color-rich / decorative / symmetric dimensions the minimalist and
  brutalist packs leave idle. Added AA note on metallic-on-jewel contrast.

- **`editorial-warm.md`** — authored to demonstrate the skill's headline claim: a
  *novel, concept-driven* style owing nothing to a named movement, derived from a
  governing concept ("a well-thumbed printed almanac on a sunny table") with the
  interpretation-not-lookup step shown explicitly in its Voice. Exercises the
  warm / soft / human dimension both other packs reject (brutalist's `not_for`
  literally excludes "consumer-warm"). Not sourced from an external spec — it's an
  original built from the `craft/` reasoning as a template proof-of-range.

## Design decisions specific to this skill

- **Pluggable style, not baked-in style.** The core insight is that minimalist and
  brutalist are two *settings* of one machine, not two skills. The 4-source style
  resolver (named built-in → described → reference image → brief-inference) all
  normalize to one **style contract** that the rest of the skill reads from.
- **Invariants above the plugin.** Accessibility, consistency locks, and honesty
  rules are enforced by the skill and clamp any style-pack value that would violate
  them — so a style can never turn off contrast/targets/reduced-motion.
- **`_template.md` is the pluggable slot.** It doubles as the authoring schema for
  new built-ins and the capture format for described / image-derived styles.
- **UX/UI split** — see `ux-principles/references.md`. This skill assumes UX is sound
  and owns look-and-feel; the AA-contrast and reduced-motion invariants are shared
  and intentionally duplicated so either skill stands alone.
- Kept **standalone**: references to `ux-principles` and any framework/component
  skill are optional ("if the project uses it"), not prerequisites.
- **Generative layer resolves the anti-slop tension.** The skill's spine works by
  *banning* (no this, no that, one accent, ≤2 layouts) — which risks producing
  "not-slop" that's also "nothing." The Step 1.5 governing-concept idea reconciles
  this: personality comes from *committing harder to one premise and subtracting*,
  which is the same discipline as the locks, not a license to add. The generative
  material is deliberately placed **below** the invariants (Step 1.5, before Step 2)
  so a concept/aesthetic choice can never turn off contrast/targets/reduced-motion.
- **`craft/` vs `styles/`.** `styles/` = *which* look (concrete token packs);
  `craft/` = *how to reason about* looks (the transferable method). The concept a
  `craft/`-guided session produces lands in the `Voice / Governing Concept` slot of
  a `styles/` contract.
