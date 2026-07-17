# craft — composition (arranging for rhythm and the eye)

Consulted from **Step 1.5** when laying out a surface. Composition is the
arrangement of elements in space: what leads, what follows, what breathes, and in
what order the eye travels. It is where a surface earns the words *elegant* or
*busy*.

**The framing that matters here:** visual hierarchy is usually taught as
*information architecture* — making the important thing findable. That's true and
it lives in the `ux-principles` layer. But hierarchy is *also* **aesthetic rhythm**:
the intervals between sizes, weights, and spaces create a cadence that the eye
finds pleasing or grating the same way an ear does with music. A surface with good
hierarchy doesn't just *work* — it feels *composed*. This file treats composition
as both at once: structure that reads clearly *and* rhythm that feels good. The two
are the same act done well.

---

## 1. Grid: the substrate everything sits on

The human eye likes to know where things will be. A grid provides that
predictability and is the fastest route from "arrangement" to "composition."

- **Design to a grid.** Columns (12 is a common web default, not a law), consistent
  gutters, a baseline rhythm for vertical spacing. Elements align to it; alignment
  is most of what separates "designed" from "placed."
- **The grid is a frame to play against, not a cage.** Strict, symmetric grids read
  as ordered and neutral (Swiss). Deliberately *breaking* the grid — one element
  that spans, bleeds, or sits off-axis — creates a focal point precisely *because*
  the grid set the expectation. You can only break a rule the viewer can feel.
- **Match grid character to the concept.** Rigid/symmetric = calm, trustworthy,
  formal. Asymmetric/loose = dynamic, editorial, energetic. This is a concept
  decision (`craft/stylization.md`), not a default.

---

## 2. Hierarchy as rhythm (the aesthetic core)

Hierarchy is built from three tools. Used well they create a *cadence*; used
timidly they create mush.

**Scale.** Bigger = more important, and the eye goes there first.
- Use **~3 sizes** (large / medium / small — headline, subhead, body). Enough to
  structure, few enough to stay clear.
- **The intervals are the rhythm.** Sizes stepped by a consistent ratio (a type
  scale, e.g. 1.25×) feel musical; arbitrary sizes feel accidental. Even spacing
  should follow a scale (4/8px base), so the *gaps* have rhythm too.
- **Amplitude creates feeling.** A big jump from headline to body (dramatic scale
  contrast) feels bold and editorial; a gentle jump feels calm and uniform. Choose
  the amplitude from the concept — timid, medium-everything contrast is the visual
  signature of slop.

**Color & contrast.** It's not the color, it's the *contrast in value/saturation*
against the surroundings that pulls the eye (see `craft/color.md` §3).
- Use no more than ~3 contrast levels (header / subhead / body). If everything is
  high-contrast, nothing leads.
- Type contrast (weight, italic) signals importance within the same family — the
  main skill's type lock: emphasize with weight/italic of the *same* face, never a
  random second family.

**Grouping (proximity & common region).** Space communicates relationship before
anything is read.
- **Tighten space *within* a group, widen it *between* groups.** A heading close to
  its content + a big gap before the next block is what makes structure legible
  without borders. This spacing contrast *is* rhythm — the eye reads the pulse of
  tight/loose/tight/loose.
- Reach for an explicit container (border/background) only when spacing alone isn't
  enough; containers add visual weight, so use them sparingly (main skill: group
  with space first, cards only when elevation means something).

**One combined rule:** pick a *small* number of levels on each axis (≈3 sizes, ≈3
contrasts) and make the steps *decisive*. Clear, rhythmic intervals are what make a
layout feel both readable and pleasing.

---

## 3. Focal point: give the eye a place to land

Every composition needs one clear entry point — the thing the eye hits first.
Without it, a "balanced" layout becomes a flat field with no way in.

- **Establish exactly one primary focal point per view.** Limit big/loud elements
  to ~2 total or they compete and cancel.
- Create it with the tools you already have: **scale** (make it biggest),
  **isolation** (give it the most space), **contrast/saturation** (the one hot
  color), or **grid-break** (the one off-axis element). Often a strong headline +
  disciplined negative space produces the focal point for free.
- If following good hierarchy, the focal point should emerge *naturally*. If you
  have to add a decorative device to force attention, the hierarchy underneath is
  probably too flat — fix that instead.

---

## 4. Negative space: the active ingredient

Space is not empty; it's a material. It is the cheapest, highest-leverage tool for
looking designed, and the one AI output most consistently underuses.

- **Give elements room to breathe.** Crowding prevents *any* element from being
  absorbed. More space around an element reads as more importance and more
  confidence.
- **Negative space is how minimalism and "premium" are actually built** — not by
  adding elegant things, but by removing until what remains has room. When a layout
  feels cheap, the fix is usually *more space*, not more stuff.
- Space is a rhythm instrument (see §2 grouping): the pattern of full and empty is
  what the eye reads as pace.

---

## 5. Layering & texture (depth and personality, used with restraint)

Devices that add richness — earn them against the concept, don't sprinkle them.

- **Layering** — overlapping elements (type over image, element crossing a grid
  line) creates depth and can guide flow. Keep legibility intact (scrim/contrast
  behind text — an accessibility floor, not optional). Layering reinforces
  hierarchy when the front layer is the thing that matters.
- **Texture** — grain, halftone, subtle gradient, pattern, paper/print artifacts.
  Texture is a strong carrier of *personality* and material concepts ("newsprint",
  "risograph"). It's also easy to overdo into noise — one deliberate texture tied to
  the concept, not decoration on everything. (Note: this is *visual* texture as a
  concept device; it never overrides the main skill's honesty rules — no fake UI
  chrome, real images over div-screenshots.)

---

## 6. The squint test (verify the composition works)

Before shipping a layout, **squint at it** (or blur it ~5–10px). This strips the
detail and reveals the raw structure:

- Does **one** element clearly dominate (the intended focal point)? Or do several
  fight?
- Do the **groups** read as distinct blocks with clear spacing between them?
- Does the eye travel in the **intended order**, or wander?
- Is the **rhythm** even — a pleasing pattern of mass and space — or lumpy and
  random?

If the blurred version has no clear leader or reads as an undifferentiated field,
the hierarchy is too flat — increase scale/contrast/spacing amplitude. Also test
with **real content**: a photo with strong color or an over-long headline can hijack
a hierarchy that worked in the wireframe. Design the template *and* the content that
fills it.

---

## 7. Composition slop to avoid

- **Flat hierarchy** — everything roughly the same size/weight/spacing; no focal
  point; the #1 "busy and generic" cause.
- **Timid intervals** — scale and spacing steps too small to create rhythm;
  medium-everything.
- **Underused space** — crowded layouts; the most common reason AI output looks
  cheap. When unsure, add space.
- **Repeated single layout** — the same block shape down the whole page (the main
  skill's zigzag>2 and three-equal-cards tells). Vary the layout families; let
  rhythm come from *contrast* between sections.
- **Forced focal points** — decorative arrows/glows/badges compensating for weak
  underlying hierarchy. Fix the hierarchy.
- **Center-everything reflex** — defaulting to centered stacks; use alignment and
  asymmetry deliberately per the concept.

---

## Handoff

Composition decisions fill the **Density/Layout** and **Elevation** slots of the
style contract (Step 1) and must serve the concept from `craft/stylization.md`.
Color choices about *what* leads the eye are in `craft/color.md`; this file is about
*where* it leads and *in what rhythm*. Structural correctness (flows, findability,
cognitive load) belongs to `ux-principles` if present — settle that there, render
the rhythm here.
