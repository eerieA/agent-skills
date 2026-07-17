---
name: ux-principles
description: >
  Framework- and style-agnostic user-experience discipline for any interface —
  web, product, dashboard, form, or marketing surface. Covers the durable
  heuristics that decide whether a design *works*: visual hierarchy, chunking,
  the Gestalt grouping principles (proximity, common region, similarity,
  uniform connectedness), scale, contrast, and signal-to-noise; a decision
  toolkit of UX laws (Hick, Fitts, Miller, Jakob, Doherty, Peak-End, Serial
  Position, Postel, Tesler, Occam, Von Restorff, Zeigarnik, goal-gradient);
  progressive disclosure, forgiveness and error-recovery, feedback timing, full
  interaction-state cycles, and accessibility as a floor. Use when asked to
  design, critique, or improve *how an interface behaves* — flows, layout logic,
  information architecture, findability, cognitive load — as opposed to its
  visual style. Self-contained; composes with a visual-design or testing skill
  if the project has one, but needs neither.
metadata:
  domain: uiux
  scope: design
  output-format: guidance
---

# UX Principles

User experience is *does the interface work* — can a person find what they need,
understand it, act on it, and recover when they slip? This skill is about that
question. It is deliberately separate from *how the interface looks*: the same UX
principles hold whether the surface is minimalist, brutalist, or a plain
enterprise form. Visual style is the job of a companion UI-design skill; this one
decides structure, flow, and cognitive load.

This skill is framework- and style-agnostic. It states principles and the
conditions under which each applies; apply them in whatever stack and aesthetic
the project uses.

## When to Use This Skill

- Deciding or critiquing a layout's **information hierarchy** — what the user sees
  first, second, third.
- Designing a **flow**: onboarding, checkout, a multi-step form, a wizard, search.
- A screen "feels cluttered / confusing / slow" and you need to name *why*.
- Choosing between design options and needing a principled tie-breaker.
- Reviewing findability, cognitive load, error handling, or accessibility.

**When this skill is not the right tool:**

- **Pure visual-style decisions** (palette, typeface, motion feel, "make it look
  premium / brutalist") — that is the UI-design skill's job. This skill sets the
  accessibility *floor* those choices must clear, nothing more.
- **Copywriting.** Good UX needs good copy, but wording craft is out of scope.
- **Backend / data-model problems** wearing a UI costume. Fix the model first.

## The Core Question, Restated

Before any principle below, state the interface's job in one sentence: *who* is
here, *what* are they trying to accomplish, and *what does success look like*.
Every principle is a means to that end. "It follows Fitts's Law" is worthless if
the user was trying to do something the screen never surfaced. Priorities rooted
in a real understanding of the user come first; the heuristics serve them.

## Part 1 — Layout Heuristics (Perception and Hierarchy)

These govern how a person's eye and attention move through a screen. They are the
most universally applicable tools here.

- **Visual hierarchy** — the user perceives importance through position, scale,
  and contrast. A good hierarchy means attention lands on the most important thing
  *first*, without the user hunting. Decide the rank order of elements, then make
  the ranking visible. What counts as "most important" is defined by the user's
  task, not by what you want to promote.
- **Chunking** — break content into small, self-contained units (a short heading +
  a concise block) instead of one undifferentiated mass. Chunked interfaces are
  easier to scan, understand, and remember. This is the first fix for "it feels
  overwhelming."
- **Scale** — use relative size to signal rank. The most important block is
  largest; within a block, the title outweighs supporting text. Scale is the
  cheapest hierarchy signal you have.
- **Contrast** — differences in type, weight, color, or background let users
  distinguish categories and predict behavior (a bright *Submit* next to a muted
  *Cancel*; a shaded table header). Contrast groups content *and* shapes
  expectations about how things work.
- **Signal-to-noise** — the content the user wants is signal; everything else is
  noise competing with it. Cut, collapse, or defer noise. Filters closed inside an
  accordion by default (open for power users, quiet for everyone else) is the
  canonical move.

### The Gestalt grouping principles

How the eye decides *what belongs with what*. Use them to express relationships
without adding chrome:

- **Proximity** — elements placed close together are read as a group; space
  between groups separates them. Whitespace is a grouping tool, not just padding.
- **Common region** — a shared boundary (a box, a background fill, a card) binds
  elements into one unit, even across distance.
- **Similarity** — elements sharing color/shape/size/orientation are perceived as
  related in *function* (why visited links differ in color from unvisited).
- **Uniform connectedness** — elements joined by a visible connector (a line, a
  frame, a shared container) read as the most strongly related of all.
- **Prägnanz (simplicity)** — people resolve complex/ambiguous forms into the
  simplest reading. Favor simple, regular shapes for interactive elements; don't
  make the user decode a clever layout.

## Part 2 — The UX Laws (A Decision Toolkit)

These are not rules to apply everywhere; each is a lens for a *specific* problem.
Reach for the one that names the situation in front of you.

**Reducing friction and choice**
- **Hick's Law** — more (and more complex) choices slow or paralyze the decision.
  When a menu, plan grid, or option list stalls users, *cut or group* the options.
- **Miller's Law** — working memory holds ~7±2 items. Don't ask users to juggle
  more at once; chunk, and don't hide a critical value they'll need three steps
  later.
- **Tesler's Law (conservation of complexity)** — some complexity is intrinsic and
  can't be deleted, only *moved*. Absorb it into the system (smart defaults,
  inference) rather than pushing it onto the user.
- **Occam's Razor** — among designs that do the job, pick the simplest. Remove
  elements until removing more would break function.

**Making targets and actions easy**
- **Fitts's Law** — time to hit a target grows with distance and shrinks with size.
  Make primary actions big, reachable, and well-separated from destructive ones;
  put frequent actions within easy reach (thumb zones on mobile).
- **Jakob's Law** — users spend most of their time on *other* sites/apps and expect
  yours to work the same way. Honor established conventions (cart in the top-right,
  logo links home) unless you have a strong, tested reason to deviate.
- **Postel's Law (robustness)** — be liberal in what you accept, strict in what you
  demand. Accept "US" for "United States" and normalize it yourself; ask for the
  minimum information needed.

**Time and perceived performance**
- **Doherty Threshold** — interaction feels effortless when the system responds in
  under ~400 ms. When real work takes longer, keep the user informed: progress
  bars, skeletons, optimistic UI. Perceived speed beats raw speed.
- **Parkinson's Law** — a task expands to fill the time allowed. Streamline so a
  task takes no longer than users expect; remembered logins, autofill, and sane
  defaults shorten it.

**Memory and motivation**
- **Peak-End Rule** — people judge an experience by its most intense moment and its
  end, not the average. Invest in the peak (the "aha") and the finish (success
  confirmation, a graceful empty/404 state).
- **Serial Position Effect** — first and last items in a sequence are best
  remembered. Put the most important nav/actions at the ends, the least important
  in the middle.
- **Von Restorff (isolation) Effect** — the item that looks different is the one
  remembered. Make the primary CTA visually distinct — but isolate *one* thing;
  if everything shouts, nothing is heard.
- **Zeigarnik Effect** — unfinished tasks stay in mind and pull toward completion.
  A visible progress checklist or a two-step signup leverages this.
- **Goal-gradient Effect** — motivation rises as a goal nears. Show progress and,
  where honest, give a head start ("2 of 5 done") to pull users forward.

**Aesthetics as a UX factor**
- **Aesthetic-Usability Effect** — users perceive visually pleasing interfaces as
  more usable and forgive minor friction. Visual polish is a UX lever, not just
  decoration — *but it never substitutes for actually working.* (The visual craft
  itself belongs to the UI-design skill.)

## Part 3 — Interaction and Flow

- **Progressive disclosure** — show the essentials by default; reveal detail and
  advanced options on demand (summary → details → advanced). Prevents Hick/Miller
  overload without hiding capability.
- **Immediate feedback** — every action gets a visible response within ~100 ms
  (press states, hover, inline validation). Silence reads as "broken."
- **Full interaction-state cycles** — design every state, not just the happy path:
  **loading** (skeletons that match final layout, not a bare spinner), **empty**
  (say how to populate it), **error** (inline and specific, with the fix),
  **success**, **disabled**. Shipping only the success state is the most common UX
  gap.
- **Forgiveness** — make errors hard and recovery easy: confirm destructive
  actions, prefer undo/soft-delete over hard delete, preserve user input on error
  (never clear a form), disable invalid actions rather than letting them fail.
- **Consistency** — similar things look and behave similarly across the product
  (all modals close the same way; primary actions sit in the same place). Users
  build a mental model once and reuse it; consistency is what makes that possible.
- **Navigation legibility** — clear structure, current-location cues, breadcrumbs
  past two levels of depth, predictable back behavior, and navigation that follows
  the user's task flow rather than the org chart.

## Part 4 — Accessibility Is a Floor, Not a Feature

These are non-negotiable minimums, independent of visual style:

- **Contrast** — WCAG 2.1 AA at minimum: 4.5:1 for body text, 3:1 for large text
  (18px+/14px bold) and meaningful UI/graphics. Aim higher for primary reading.
- **Never rely on color alone** to convey information — pair it with an icon, label,
  or shape (color-blind users, grayscale contexts).
- **Touch targets** ≥ 44×44 px, with adequate spacing between them.
- **Keyboard operable** — every interactive element reachable and usable by
  keyboard, in a logical tab order, with a *visible* focus state.
- **Semantic structure** — real headings, landmarks, labels, and alt text so
  assistive tech can parse the page; ARIA only where semantic HTML can't express it.
- **Respect user preferences** — honor `prefers-reduced-motion` and
  `prefers-color-scheme`; don't trap users in one mode.
- **Test with real users, including users with disabilities.** Heuristics predict;
  observation confirms.

## Part 5 — Designing for Maturity (When the Product Will Grow)

For interfaces expected to live and expand (internal tools, platforms, long-lived
products), add two lenses drawn from mature-product practice:

- **Scalability** — will this layout still make sense with 10× the data, more
  features, more roles? Design for growth: filtering/search that scales, room to
  add without a rebuild, and complexity that stays hidden until needed. A pattern
  that only works at today's volume is technical debt.
- **Consistency at system scale** — as surfaces multiply, uniform components,
  tokens, and interaction patterns are what keep the product learnable. Define the
  pattern once; reuse it everywhere. (The UI-design skill's *style contract* is one
  way to hold this line.)

## Relationship to Other Skills

This skill is self-sufficient — it needs no other skill present. References below
are optional: when a project *also* uses the named skill, the two compose; when it
doesn't, ignore the reference and proceed with this skill alone.

- **`ui-taste`** (if the project uses it) — owns the *visual* layer: brief-read,
  aesthetic style (pluggable), palette/typography/motion craft, and the anti-slop
  discipline. This skill decides whether a design *works*; that one decides how it
  *looks and feels*. They pair naturally: settle hierarchy, flow, and states here;
  render them there. Accessibility contrast/motion invariants are shared and appear
  in both.
- **`testing-discipline`** (if the project uses it) — usability testing is the
  empirical check on the heuristics above. This skill tells you what to look for;
  that one shapes how to verify it.

## Verification Checklist

- [ ] The interface's job — who, what, success — is stated in one sentence
- [ ] Visual hierarchy matches task importance; the most important thing is seen first
- [ ] Content is chunked; signal is separated from noise
- [ ] Grouping (proximity/region/similarity) reflects real relationships
- [ ] Choice and cognitive load are bounded (Hick/Miller); complexity is absorbed, not dumped (Tesler)
- [ ] Primary actions are large, reachable, distinct; conventions honored (Fitts/Jakob/Von Restorff)
- [ ] Feedback is immediate; long waits are covered (Doherty); perceived speed addressed
- [ ] Every interaction state exists: loading, empty, error, success, disabled
- [ ] Errors are hard to make and easy to recover from; input is preserved
- [ ] Accessibility floor met: AA contrast, not color-alone, 44px targets, keyboard + visible focus, semantics, reduced-motion/color-scheme
- [ ] If the product will grow: the layout and patterns scale without a rebuild
