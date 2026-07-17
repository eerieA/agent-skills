# references — ui-style-guide

Author-only memory-jog for what this skill was built on. Not part of the skill;
leave out when copying the skill into a project.

## Sources

- **"Design system 101: What is a design system?"** (Figma blog)
  (https://www.figma.com/blog/design-systems-101-what-is-a-design-system/)
  — source of the altitude model (Step 1): the design-system hierarchy (system →
  component/pattern libraries → foundational elements), the style-guide-vs-design-
  system distinction (a style guide is the visual subset; a system adds standards,
  governance, code linkage), and the "do you even need one" judgment (systems exist
  to stop inconsistency *at scale* — overhead without scale). Also the "single
  source of truth / reduce redundancy / onboarding" rationale for Step 5.

- **"4Paws" style guide by (Behance)**
  (https://www.behance.net/gallery/100160917/4Paws-Online-veterinary-cards-service)
  — compact style-guide example. Source of the concrete component-inventory
  discipline in Step 4: inputs shown empty → filled-valid(✓) → error(✗), password
  reveal, dropdowns closed → focused → open, toggles on/off, filled vs. outline
  buttons, icon size tiers (16/20/40pt), logo lockups. The state-by-state
  completeness is the lesson taken from it.

- **"Style Guide" by Chike Opara (Behance)**
  (https://www.behance.net/gallery/153767697/Style-Guide)
  — full UI style-guide example. Source of the indexed multi-section structure
  (Step 5) and the token rigor (Step 3): an explicit contents index; Colors split
  into brand / state / black / grey roles; a typography table with font size **and
  line height** per level; dedicated Grid Systems and Spacing sections shown as
  specimens; Iconography; and a deep component ladder (Textfields, Selectors,
  Buttons, Small Elements, Big Elements incl. tables/banners/modals, Cards).

## Design decisions specific to this skill

- **New skill, not folded into `ui-taste`.** Different verb and different output:
  `ui-taste` *styles a surface* (decides the look); this skill *documents a system
  and builds a reusable component inventory* (systematizes a look already decided).
  Folding would overload `ui-taste` and blur its "when to use." Clean directional
  pipeline instead: ui-taste resolves the language → ui-style-guide documents/
  componentizes it → screens are built against the guide.
- **Different temperament, kept separate on purpose.** `ui-taste` is
  artistic-but-logical and deliberately anti-rigid (grid *mechanics* were kept out
  of its style packs). This skill is the rigorous, exhaustive counterpart — token
  taxonomy, full state coverage, spacing/grid specimens. The mechanical grid the
  ui-taste packs omit lives *here* (Step 3f), tied to breakpoints.
- **Completeness is the product.** The core discipline (Step 4) is every component
  in every state; a guide that omits disabled/loading/focus states has failed its
  one job. Framed harder than in either source example.
- **Altitude-gated (Step 1).** Token sheet / style guide / design system — match to
  real scale; over-systematizing a small project is called out as a failure mode
  (straight from the Figma design-system-101 "do you need one" section).
- **Shared invariant.** The WCAG AA floor is duplicated here (Step 6) as in
  `ui-taste` and `ux-principles`, so the skill stands alone — and a guide is the
  place to *prove* contrast, not just claim it.
- **Artifact as output medium.** A self-contained HTML Artifact is the natural
  render target (it can live-show every token/component/state); noted in Step 5.
  `output-format: artifact` in the frontmatter reflects this.
- The `tmp-4paws.jpg` and `tmp-sg-by-chike-opara.jpg` files in `skills/uiux/` are
  the user's raw source images for this skill; the durable sources are the Behance
  URLs above. The temp images can be deleted once this is settled.
