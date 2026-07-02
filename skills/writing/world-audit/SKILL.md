---
name: world-audit
description: >
  Audit an existing fiction world for coherence and craft. The writer pastes or
  points at their world notes / world bible / draft; this scans for missing rules,
  internal contradictions, unbounded magic or tech, infodump risk, thin sensory
  detail, and genre-specific failures. Produces a prioritized findings table, then
  helps fix what the writer approves. Invoke with /world-audit.
---

Review a writer's existing story world for the things that make a world feel fake,
inconsistent, or story-killing. This is the critique counterpart to
`/world-building`. Do not rewrite their world or impose your taste — find concrete
problems and propose targeted fixes.

## Intake

Ask the writer to provide their world material (bible, notes, or a draft) and, if
not obvious, the **premise/logline** and **genre**. You cannot judge whether the
world serves the story without knowing the story, and you can't apply the right
genre lens blind. If they give a draft rather than notes, audit the world *as it
appears on the page*, which also lets you judge delivery (categories 5–6 below).

## Audit checklist

Work through each category. For each finding, record:
- **Location** — file:line, section name, or a short quote so they can find it
- **Severity** — High / Medium / Low (see definitions)
- **Category** — which one below
- **What goes wrong** — the concrete failure, not just the label
- **Suggested fix** — one line

Present findings as a markdown table grouped by severity. After the table, ask
which findings to address before changing anything.

---

### 1. Missing or toothless rules (High)

The world has no hard rules, or its "rules" are flavor that generate no conflict.
Without rules the story has no boundaries and problems can be solved from nowhere.

Look for:
- No stated limits on what magic/tech/power *can't* do
- "Rules" that constrain nothing and create no problem for anyone
- More than ~10 tracked rules (too many to stay consistent)

**Fix pattern:** for each core power/system, state its limit, cost, and failure
condition. For each rule, name the conflict it generates; if none, demote it from
rule to flavor.

---

### 2. Internal contradictions / broken coherence (High)

Elements that can't both be true. A world loses credibility the instant its causal
chain breaks.

Look for:
- Climate/geography vs. crops vs. food vs. clothing mismatches
- History that doesn't fit the present government or power structure
- Transportation/tech that doesn't match the landscape or economy
- A rule stated in one place, silently violated in another
- Timeline or genealogy that doesn't add up

**Fix pattern:** surface the contradicting pair and propose the smaller change that
restores the chain (history → government → economy → daily life should be one
causal line).

---

### 3. Unbounded power (High)

Magic or technology powerful enough to trivialize the central conflict, with no
cost or limit — the story resolves itself.

Look for:
- Abilities with no stated cost, cooldown, or failure mode
- A power that could solve the protagonist's core problem but conveniently isn't
  used (reader will notice)
- Escalating capabilities that outrun the stakes

**Fix pattern:** add a cost, a limit, or a condition of failure that keeps the
central problem hard. Prefer a limit that itself generates story.

---

### 4. The world eating the story (Medium)

Elaboration far beyond what the premise needs — the classic rabbit hole. Signals
over-building and often masks avoidance of writing the actual story.

Look for:
- Deep systems (languages, genealogies, economies) with no bearing on the premise
- Lore volume wildly out of proportion to story scope
- A world so complex a reader would need a flow chart

**Fix pattern:** flag as scaffolding, not error — recommend demoting to an
"open questions / deep lore" appendix and refocusing on story-serving material.
Never delete their work; reclassify it.

---

### 5. Infodump risk (Medium — draft only)

World information delivered as a lecture rather than woven into scene. Applies when
auditing prose, not private notes (notes are *supposed* to be raw).

Look for:
- Paragraphs of history/mechanics that stop the story to explain
- A new concept introduced by definition rather than through a character's reaction
- Several strange elements dropped at once with no familiar landmark

**Fix pattern:** convert to need-to-know delivery — introduce one new thing at a
time, against familiar landmarks, through how characters react to it (cf. how
readers meet the direwolf via the pony and kennel dogs they already know).

---

### 6. Thin or abstract rendering (Medium — draft only)

Setting told in the abstract ("it was a terrible place") instead of shown in
specific sensory detail, so the reader's mind can't build the world.

Look for:
- Abstract adjectives (terrible, beautiful, magical) doing the work detail should
- Places described with zero sensory specifics
- Setting used as neutral backdrop, disconnected from the viewpoint character's mood

**Fix pattern:** replace abstraction with ~3 concrete qualities per key object
("a dark blue carpet"), engage more than sight, and tie the description to whose
eyes we're in — setting should reflect or resist their mood.

---

### 7. Genre-specific failures (varies)

Apply the lens matching the work's genre:
- **Fantasy** — anachronisms; magic that reshapes combat but implausibly leaves
  economy/power untouched; magic-as-plot-convenience.
- **Sci-fi** — inconsistent physics (FTL/AI/biotech rules that shift); missing
  second-order social effects of the technology.
- **Contemporary / historical** — factual/research errors and period anachronisms
  that break a knowledgeable reader's trust; generic "postcard" rendering of a
  real place or subculture instead of lived-in specifics.
- **Horror** — an unbounded threat (no rules for what it can/can't do or what wards
  it off), which reads as arbitrary rather than frightening.

**Fix pattern:** name the specific breach and the minimal correction; for research
errors, flag what needs verifying rather than guessing.

---

## Severity definitions

| Severity | Meaning |
|----------|---------|
| High | Breaks credibility or kills story tension (contradictions, unbounded power, no rules) |
| Medium | Weakens immersion or signals over-building; fixable without structural damage |
| Low | Minor polish; missed opportunity, no real harm |

---

## After presenting findings

1. Show the findings table, grouped by severity.
2. Ask: "Which findings should I work on? (e.g. 'all High', 'items 1 3 5', 'skip the draft-only ones')"
3. Address only what the writer approves — one finding at a time, showing the
   before/after or the concrete suggestion.
4. Don't restructure their bible, rename things, or add lore they didn't ask for.
   Keep the world theirs.
