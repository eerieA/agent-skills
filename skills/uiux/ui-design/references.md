# references — ui-design

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
