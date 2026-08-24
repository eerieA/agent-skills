---
name: docs-prose-compaction
description: >
  Compact documentation and code prose — code comments, engineering docs, reports,
  runbooks, commit messages, PR descriptions, UI copy — by cutting what a competent reader
  recovers for free, while defending every load-bearing fact. For reference prose, which
  is consulted rather than read through, and where a sentence is cuttable when the reader
  recovers it from the code, the signature, or the sentence before it. NOT for narrative
  or fictional prose, where cutting serves rhythm, voice, and implication, and a sentence
  a reader could infer is often the one doing the most work. Point it at a file, a diff, a
  comment block, or a paste. It classifies each sentence as fact / derivable / narration /
  stamp / flourish, cuts the last four tiers, and leaves the first alone no matter how
  long it runs. Catches
  the standard bloat patterns: restating the consequence of a fact just given, narrating
  what the code plainly does, per-branch enumerations that duplicate the branches,
  verification stamps and dates that belong in a ledger, hedge stacking, parenthetical
  cross-references, and the same rationale duplicated in two files that then drift apart.
  Length is judged against reader cost, not a word budget — a long comment carrying a
  gotcha is correct at any length. Produces a per-block findings table with a proposed cut,
  then applies only what the writer approves. Invoke with /docs-prose-compaction.
metadata:
  domain: writing
  scope: review
  output-format: findings-table
---

Compact technical prose without losing information. This is a **detect-and-advise**
skill in the same family as `ai-tell-audit`: classify, propose, let the writer decide.
Do not rewrite for style, impose a voice, or shorten prose that is already carrying its
weight.

The governing idea: **a sentence earns its place by telling the reader something they
cannot recover from what they already have.** What they already have is the code beside
the comment, the sentence before this one, the type signature, the identifier names, and
their own competence. Everything recoverable from that set is cost without payload — it
takes reading time, and it goes stale independently of the thing it restates.

This is *not* a brevity skill. Compaction and brevity point the same direction only
sometimes. A twelve-line comment recording why a plausible change is wrong is correct at
twelve lines; cutting it to four to look tidy is a regression, and the skill should say
so. The target is **information per line**, and the way to raise it is almost always to
remove lines that carry none — not to compress lines that do.

## Why this matters beyond aesthetics

Redundant prose is a **correctness** problem, not a tidiness one. Two statements of the
same fact are two things to update; whichever is missed becomes a lie that reads as
authoritative. A comment saying "returns null when the list is empty" beside code that
was changed last year to throw is worse than no comment, because a reader trusts it and
stops reading the code. Every duplicated sentence is a future contradiction with a
coin-flip deciding which copy wins.

So the first question is never "is this too long?" It is **"how many places does this
fact live, and what happens when one of them changes?"**

## Intake

Ask for the target (file, path range, diff, or paste) and, if not obvious:

- **Genre** — code comment, engineering doc, upstream report/ticket, runbook, commit
  message, PR description, or user-facing copy. The cut rules differ; see
  `craft/genres.md`.
- **Audience** — a teammate who knows the codebase, a future maintainer who does not, or
  an external reader (upstream API team, client). Audience decides what counts as
  "recoverable for free": an external reader recovers much less, so more survives.
- **Provenance** — the writer's own prose, or machine-generated text being cleaned up.
  Be more aggressive on the latter, more conservative on the former.

If unspecified, assume code comment, teammate audience, and be conservative.

## The classification

Every sentence lands in exactly one tier. The tier decides the verdict.

| Tier | What it is | Verdict |
|------|-----------|---------|
| **Fact** | Information not recoverable from the surrounding context — behaviour of another system, a measured number, a decision's *why*, a gotcha that still bites, a guard against a plausible-but-wrong change | **Keep**, at any length |
| **Derivable** | A true statement the reader reconstructs for free from a fact already given, the code beside it, or the type signature | **Cut** |
| **Narration** | Describes what the code plainly does, in prose, in the same order | **Cut** |
| **Stamp** | Dates, version numbers, "verified by X on Y", commit hashes, build status, progress | **Cut** from code and structural docs; relocate to whichever ledger owns status |
| **Flourish** | The concluding flourish, the editorial verdict, the restated thesis, self-praise for the design | **Cut** |

The judgment call is almost always **fact vs. derivable**, and the test is a question
about the reader, not the sentence: *given the line above and the code below, would a
competent reader who did not have this sentence be missing anything?* If no, it is
derivable regardless of how true or well-written it is.

`craft/patterns.md` is the catalog of what each tier looks like in practice, with
before/after pairs. `craft/keep-rules.md` is the counter-catalog — what must survive,
and it is the more important of the two. Read `craft/keep-rules.md` **before** writing
any finding.

## Workflow

1. Read the target once whole, for genre and what it is *for*, before cutting anything.
2. Split into blocks — a comment block, a doc section, a paragraph.
3. Per block, classify each sentence into the five tiers above.
4. Check every proposed cut against `craft/keep-rules.md`. This is the over-correction
   guard and it has veto power.
5. For surviving findings, record: **location**, **tier**, **the sentence**, **why it is
   recoverable** (name the source — "the `if` below", "the return type", "the previous
   sentence"), and **the proposed replacement block**.
6. Present as a table grouped by block, then a proposed diff per block.
7. Ask which to apply. Apply only those. Show before/after.

Report the reduction as **lines removed and what class they were**, never as a
percentage or a quality score. "Cut 6 lines: 4 derivable, 1 stamp, 1 flourish" is
actionable. "38% more concise" is not, and invites cutting to hit a number.

## Cutting discipline

- **Cut whole sentences, not words.** Compressing a load-bearing sentence into a denser
  one costs clarity and saves nothing worth having. Either the sentence carries a fact
  (leave it in full) or it does not (delete it entirely). Word-level tightening is a
  different activity and mostly not worth doing.
- **Never trade a fact for a line.** If a cut loses information, it is not a cut, it is a
  deletion. Reject it.
- **Reflow after cutting.** Once sentences are gone, rewrap the block. Fewer, fuller
  lines beat preserved line breaks around a hole.
- **One owner per fact.** When the same rationale appears in two files, do not trim both
  — pick the file that *owns* it (the one whose code the fact is about), leave that copy
  whole, and replace the other with a pointer. Two half-statements are worse than one
  full one plus a reference.
- **Preserve exactly** — never touch: code, identifiers, URLs, paths, commands, env vars,
  version numbers *inside a technical claim*, error strings, table structure, headings,
  frontmatter. Compaction operates on prose between these.
- **A pointer is not a summary.** `see X` replacing a fact is a loss unless X genuinely
  holds it. Verify the target says what you are claiming it says before pointing there.

## The standard bloat patterns

Summarized here; full catalog with examples in `craft/patterns.md`.

- **Consequence restatement** — states the fact, then states what it implies. The
  implication is free. *The single most common pattern in machine-written comments.*
- **Branch enumeration** — "Step 1 needs a name; Step 2 needs a pair; Steps 3/4 always
  pass" above the three `if`s that say exactly that.
- **Signature narration** — "returns a string when invalid, else null" above
  `: string | null`.
- **Verification stamp** — "verified by introspection 2026-07-29". The claim stays, the
  receipt goes to the ledger.
- **Hedge stack** — "generally", "in most cases", "typically" layered onto one claim.
  Keep at most one, and only if the uncertainty is real and load-bearing.
- **Parenthetical cross-reference** — "(mapped by the wizard's `triggerErrorMessage`)".
  A reader who needs it greps; everyone else pays a line.
- **Emphasis inflation** — seven CAPS or bold spans in one block. Emphasis is
  positional: when everything shouts, the one real footgun stops standing out. Cut to
  the two or three that mark actual traps.
- **The closing verdict** — "Greying the option is what makes the wizard honest." The
  preceding lines already earned it.
- **Restated preamble** — a doc section that opens by summarizing what the section is
  about, before saying it.

## Structural compaction

Beyond the sentence, three moves that shrink documents more than any sentence work:

- **Prose → table** when the text enumerates parallel items with the same attributes.
  Four "X does A, taking B" sentences become four rows and stop drifting in phrasing.
- **Merge sections that answer the same question.** Two headings the reader cannot
  distinguish means one section split by accident.
- **Delete the section that restates the document.** Overviews that summarize what
  follows, and conclusions that summarize what preceded, are both derivable — unless the
  document is long enough that the overview is genuinely a map (then keep it and cut the
  conclusion).

Sequencing matters: **do structural cuts before sentence cuts.** Carefully compacting
prose inside a section you then delete is wasted work, and it biases you toward keeping
the section because you just invested in it.

## Two audiences, one document

Technical writing standards (IEC/IEEE 82079-1 and its lineage) make a point worth
borrowing without borrowing their machinery: **information must be findable, minimal in
each task, and complete overall** — three demands that conflict unless the document is
structured so a reader takes only the path their task requires. The portable lessons:

- **Write to the task, not to the topic.** A block a reader consults while making a
  change should tell them what they need for *that change*, not everything true about
  the subject. Reference material for other tasks moves out of the path.
- **Completeness lives at the document level, minimality at the block level.** A fact is
  not "missing" because a given comment omits it; it is missing if no reachable place
  holds it. This is what licenses aggressive cutting *with* a pointer, and forbids
  cutting *without* one.
- **Instructions carry only what changes the action.** In a runbook step, anything that
  does not change what the operator does next is commentary. Warnings are the exception
  and they precede the step they guard, never follow it.
- **Say it once, in the place the reader is when they need it.** Restating a caution in
  three sections means three copies to maintain and a reader who learns to skim
  cautions.
- **Identical things get identical words.** Compaction pressure tempts elegant variation
  ("the trunk" / "the LAG" / "the port-channel" for one object). Synonym rotation is not
  concision; it is a second thing to disambiguate. Fix the term, repeat it.

## What this skill will not do

- Hit a length target, or report a compression percentage.
- Shorten a comment that records a gotcha, a decision's *why*, or a guard against a
  plausible-wrong change. These are the reason comments exist.
- Rewrite for tone or voice — that is `ai-tell-audit`.
- Restructure code, rename identifiers, or change behaviour.
- Cut prose in files the project marks as owned elsewhere (upstream specs, contracts,
  other teams' docs). Read-only means read-only; report, do not edit.
- Delete a fact because it is inconvenient to place. Unplaceable facts get raised with
  the writer, not dropped.
