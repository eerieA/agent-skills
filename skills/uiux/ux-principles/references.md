# references — ux-principles

Author-only memory-jog for what this skill was built on. Not part of the skill;
leave out when copying the skill into a project.

## Sources

- **"Design Principles: UX design basics for site managers"** (Heidi Strohl, McGill
  Web Services)
  (https://www.mcgill.ca/web-services/design-principles-ux-design-basics-site-managers)
  — backbone of Part 1 (layout heuristics): chunking, proximity and region, scale,
  visual hierarchy, contrast, signal-to-noise. The most succinct, universally
  applicable framing of the perceptual principles, which is why it anchors that part.

- **"The 21 most influential UX laws" / Laws of UX** (Maze, curating Jon Yablonski)
  (https://maze.co/collections/ux-ui-design/ux-laws/)
  — source of Part 2 (the UX-law decision toolkit): Jakob, Aesthetic-Usability,
  Doherty, Fitts, Hick, Miller, goal-gradient, the Gestalt grouping laws (common
  region, proximity, uniform connectedness, Prägnanz, similarity), Occam, Pareto,
  Parkinson, Peak-End, Postel, Serial Position, Tesler, Von Restorff, Zeigarnik.
  Adapted, not copied: each law was rewritten as a "reach for this when…" lens with
  the marketing examples stripped, and Pareto was folded into general prioritization
  rather than given its own entry.

- **"Key UI/UX design principles"** (Microsoft Learn, Dynamics 365 guidance)
  (https://learn.microsoft.com/en-us/dynamics365/guidance/develop/ui-ux-design-principles)
  — source of Part 5 (designing for maturity): Scalability and Consistency-at-scale,
  plus reinforcement of user-centricity, simplicity, and efficiency. Deliberately
  mined only for the durable, product-agnostic lessons; the Dynamics/Power-Apps and
  model-driven/canvas specifics were dropped as too opinionated and vendor-bound.

- **`bencium-controlled-ux-designer` SKILL.md** (bencium-marketplace)
  (https://github.com/bencium/bencium-marketplace/blob/main/bencium-controlled-ux-designer/skills/bencium-controlled-ux-designer/)
  — source of the UX-side content in Part 3 (progressive disclosure, immediate
  feedback, forgiveness/error-recovery, consistency, full interaction-state cycles,
  navigation legibility) and the accessibility floor in Part 4. Its *visual*-design
  and stack-specific material (color/type/motion craft, shadcn/Tailwind/Phosphor
  defaults, MOTION-SPEC.md, RESPONSIVE-DESIGN.md) was routed to `ui-design` instead,
  keeping this skill style-agnostic.

## Design decisions specific to this skill

- **UX / UI split.** This skill deliberately owns only *does it work* — hierarchy,
  flow, cognitive load, findability, accessibility rationale. All *how it looks*
  content (palette, typography, motion feel, anti-slop) lives in `ui-design`. The
  split lets this skill stay framework- and style-agnostic and apply to dashboards
  and forms, not just marketing surfaces.
- **Laws as a toolkit, not a checklist.** The 21 laws are framed as situational
  lenses ("reach for the one that names your problem") rather than rules to apply
  everywhere, to avoid cargo-culting.
- **Accessibility as a floor.** Stated as hard minimums independent of style, with
  the AA-contrast and reduced-motion invariants intentionally duplicated into
  `ui-design` so either skill enforces them standalone.
- Kept **standalone**: references to `ui-design` and `testing-discipline` are
  optional ("if the project uses it"), not prerequisites.
