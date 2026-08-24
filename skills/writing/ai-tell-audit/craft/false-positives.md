# False positives - what is NOT a tell

The over-correction guard. Consult this **before** writing any finding. The failure
mode of this skill is gutting legitimate human prose because it pattern-matched a
coincidence. When unsure, do not flag.

## The cluster rule

A clean human writer hits many patterns in `patterns.md` without any AI involvement.
No single Medium/Low tell is evidence. Flag when tells **cluster** - several near
each other, or one pattern repeated - not when one appears alone.

A single em dash means nothing. Em dash **+** rule-of-three **+** "vibrant tapestry"
**+** a "Conclusion" section is a confession.

## Not reliable indicators on their own

- **Polished grammar and consistent style.** Many writers are professionals or have
  been edited. Polish is not AI.
- **Mixed casual/formal register.** Often signals a technical person, a young writer,
  or neurodivergent prose habits - not a chatbot.
- **"Bland" or "robotic" prose.** AI has *specific* tells. Generic dryness without
  them is just dry writing.
- **Formal/academic vocabulary.** AI overuses *specific* fancy words, not all of
  them. Don't flatten *ostensibly* or *constituent* for sounding brainy.
- **One transition word.** *Additionally / moreover / however* are tells only when
  piled up. One *however* is not.
- **Curly quotes alone.** macOS, Word, Google Docs, most CMSes auto-curl by default.
- **Em dashes alone.** Many editors and journalists use them heavily. Evidence only
  when paired with formulaic, sales-y rhythm.
- **One short emphatic sentence.** Humans use clipped sentences to land a point. Flag
  staccato drama only when several fragments run together.
- **"Honestly" / "look" mid-sentence.** Ordinary in casual writing. The tell is the
  standalone theatrical opener, not the word.
- **Unsourced claims.** Most of the web is unsourced. Absence of citations proves
  nothing.
- **Clean, complex formatting.** Templates and visual editors produce tidy output
  with no AI.

## Never touch (secondhand text)

Do not rewrite a watched phrase when it appears inside:
- Quotations, titles, proper names, or examples where the phrase is being *discussed*
  rather than *used*.
- Code, URLs, paths, commands, frontmatter (see the preserve-exactly list in
  `SKILL.md`).

## Load-bearing clauses are not over-explanation

The guard for the **E group**. Over-applied, E2 and E4 strip the one thing a piece of
writing cannot regenerate. What that thing is depends on register, so the keep-test
comes in two forms. Both ask the same underlying question: **does this clause add
something the reader cannot get without it?**

### Technical registers - the thing to protect is *why*

Over-applied here, the E group removes what good engineering docs exist to carry. This
repo's CLAUDE.md requires it: a comment recording a gotcha or a decision's *why* "is
correct at any length".

| Keep | Cut |
|---|---|
| A **guard** against a plausible-but-wrong change (*don't select X; it needs two sweeps*) | Defending a choice already made against a reader who wasn't arguing |
| A **gotcha** that still bites (*missing this 401s the health panel*) | Restating the point in different words |
| Why a **non-obvious** option was chosen over the obvious one | Rating the choice (*the natural fit*, *exactly right*) |
| A **consequence** the reader can't derive (*this drops unsaved work*) | Pre-empting an objection nobody raised |
| Evidence for a claim someone will doubt (*bitten by this once already*) | Explaining why the rule you just wrote is a good rule |

Concretely: *"⚠️ `/health-endpoint` needs `credentials: 'include'` - miss it and the
status panel 401s"* is a **keep**. The consequence is not derivable and prevents a real
bug. But *"...and that would be wrong in the dangerous direction, since it reads as
'that doesn't exist' while someone may still be using it"* appended to an already-clear
instruction is a **cut**.

### Expressive registers - the thing to protect is *voice and implication*

In fiction, essays, and personal writing there are no gotchas to preserve, and the
keep-test changes accordingly: a clause earns its place by doing **tonal or
characterizing** work, not by preventing a mistake. The failure mode here is the
opposite of the technical one - not a lost gotcha, but prose planed down to competent
flatness. A hedging clause may be the narrator hedging *in character*; cut it and you
have edited the person, not the sentence.

| Keep | Cut |
|---|---|
| A qualifier that **reverses or complicates** the sentence (*She said nothing, and went on drying the plate*) | A qualifier that only confirms the reader read correctly (*which was not the same as agreeing*) |
| **Judgment that reveals the judge** - a narrator with opinions, in first or close third | Judgment from the authorial seat, grading the material (*a genuinely remarkable meal*) |
| A **digression, aside, or self-correction** in the writer's own voice | Narration that glosses the beat the scene just landed |
| Deliberate **repetition for rhythm or incantation** | Restating the image in plainer words in case it missed |
| **Overwriting that is the character's** - a florid narrator, an unreliable one | Overwriting that is nobody's, decorating a neutral narration |

Concretely: *"He put the photograph back in the drawer"* is finished. The appended
*"though not because he had stopped wanting to look at it"* is a **cut** - it explains
the gesture the gesture already made. But in a narrator established as compulsively
self-explaining, that same clause is characterization; keep it and flag nothing.

### When a clause could read either way, leave it

True in both registers, for different reasons. A doc that over-explains is mildly
annoying; a doc that lost its only record of why is a bug waiting to happen. A story
that over-explains is mildly annoying; a story edited into voicelessness is no longer
the writer's. The cost of a wrong cut is always higher than the cost of a wrong keep.

## Register overrides voice findings

The Voice-tier tells (C-group) are **correct writing** for reference/technical/legal
text. Neutral, plain, opinion-free prose *is* the human voice there. Only flag
soullessness, missing first person, or absent opinion when the register is expressive
(essay, blog, personal, marketing). Injecting personality into an API doc is itself a
defect.

## Signs of a real human writing (lean toward leaving it alone)

- **Specific, hard-to-fabricate detail** - a real address, an odd quote, "the lawyer
  upstairs from my dentist". LLMs round specifics off; humans hoard them.
- **Mixed feelings, unresolved tension** - "mostly good, but it bothers me and I
  can't say why." LLMs default to clean takes.
- **Dated, era-bound references** - slang, memes, in-jokes tied to a year and
  subculture. Models lag.
- **Variety in sentence length** - real writing alternates short and long; AI trends
  to an even mid-length cadence.
- **Genuine asides and self-corrections** - "(I keep wanting to say 'almost' here,
  but it really was certain.)"
- **A choice the writer could defend.** If they can say *why* they cut a word or
  used one, that's a strong human signal.

When these are present, the prose is doing something a model rarely does. Preserve
it, even if it also trips a pattern.
