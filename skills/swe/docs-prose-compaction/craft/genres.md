# Per-genre cut rules

The classification in `SKILL.md` is constant; what counts as **derivable** shifts with
genre, because each genre gives the reader a different amount of surrounding context for
free. A code comment sits next to the code — so the code is free, and restating it is
narration. A ticket sits in someone else's inbox — nothing is free, and the same sentence
is essential.

Ordered from most context-rich (cut hardest) to least (keep most).

---

## Code comments — cut hardest

The reader has the code, the identifiers, the signature, and the file. All free.

**Cut:** branch walk-throughs, signature narration, consequence restatement, sort/filter
descriptions, parenthetical cross-refs to easily-grepped names.

**Keep:** other systems' behaviour, the *why*, guards, gotchas, invariants a caller
cannot see, load-bearing precision.

**Genre-specific trap:** the comment that explains *this* function while the reader's
actual question is about its *caller*. Facts about how a function is used belong at the
call site or in the module header — moving them beats cutting them.

Module/file headers earn more length than function comments: they are the only place a
cross-cutting fact fits, and a reader lands there deliberately.

---

## Engineering docs, conventions, architecture notes

The reader has the repo but not necessarily the specific file. Cross-references work
here; they are the mechanism that lets each doc stay minimal.

**Cut:** overviews restating the body, conclusions, per-file narration recoverable by
opening the file, status/progress (a ledger owns it), rationale duplicated from a code
comment.

**Keep:** decisions and their rejected alternatives, cross-repo facts, the trigger for
revisiting a decision, anything measured.

**Genre-specific trap:** these docs attract status. "Currently implemented for EVPN-A
only" reads as structure but is progress, and rots silently. Route it to the ledger and
leave the structural claim.

Prefer **prose → table** here more than anywhere else. Convention docs are usually
enumerating parallel cases.

---

## Upstream reports, tickets, bug filings

The reader is outside the repo. **Almost nothing is free.** This genre is where
compaction instinct does the most damage.

**Cut:** internal deliberation ("we first thought X, then realised Y" — unless the wrong
path is itself instructive), restated diagnosis in three sections, our own hedging about
whether to file, praise for the API team.

**Keep:** repro steps in full, exact error strings, ids and run identifiers, the precise
claim, every citation with file and line, and explicitly-withdrawn prior diagnoses.

**Genre-specific trap:** a correction to an earlier version of the report looks like
history and reads like a candidate for cutting. It is not — if anyone read the old
version, the withdrawal is load-bearing, and dropping it lets a harmful recommendation be
re-adopted. Keep withdrawals; cut only the narrative of how the correction was reached.

Structure carries more weight than concision here: title, one-line claim, then evidence.
A reader who stops after two lines should still have the point.

---

## Runbooks and manual-testing recipes

The reader is **executing while reading**, often under time pressure.

**Cut:** anything that does not change what the operator does next. Background, rationale
for the procedure's design, alternative approaches.

**Keep:** every command verbatim, expected output, the failure branch, prerequisites, and
warnings.

**Genre-specific rules:**

- **Warnings precede the step they guard**, never follow it. A caution after the
  destructive command is decoration.
- **One step, one action.** Two actions in one numbered step means a half-done state when
  someone is interrupted.
- **State the expected result** for any step whose success is not self-evident. This looks
  like narration and is not — it is how the operator knows to continue.
- **Ground rules earn their length.** Environment facts ("`lag` is unset on all border
  interfaces on dev") prevent an operator diagnosing a non-bug. Keep in full.

---

## Commit messages and PR descriptions

The reader has the diff. Anything the diff shows is free.

**Cut:** file-by-file listings, restated diff, "refactored for clarity" with no content,
test-passing announcements (CI reports that), self-assessment.

**Keep:** *why*, the non-obvious consequence, what was deliberately left out, breaking
changes, and the reason for a surprising choice.

The subject line is the highest-leverage sentence in the repo — it is read hundreds of
times in `git log` and never edited. Spend effort there and cut the body.

---

## User-facing copy — tooltips, errors, empty states

Read mid-task, under mild frustration, by someone who will not read twice.

**Cut:** explanation of internals, apology, anything that does not help the user decide
what to do now.

**Keep:** what happened, and what they can do. Two clauses, usually.

**Genre-specific traps:**

- **Never assert something the user can see is false.** A tooltip claiming no eligible
  option exists, shown to someone looking at one, destroys trust in the whole surface.
  Compaction pressure encourages exactly this — the shorter phrasing is often the
  over-claim. Prefer the longer honest sentence.
- **Lead with the consequence, demote the cause.** "Cannot be created here yet — the
  request would classify as EVPN" beats a cause-first ordering the user must parse.
- **A pointer is not available.** The user cannot grep. Anything they need is in the
  string or unreachable.

---

## Memory files and session notes

Read by a future agent with no conversation context.

**Cut:** the conversation's shape, what was tried and abandoned, restated code the repo
already holds.

**Keep:** the non-obvious conclusion, resolved-to-absolute dates, and *why* it was
surprising enough to record.

**Genre-specific trap:** these rot faster than any other genre, because they describe a
moving target from outside it. Prefer a fact about intent (which the repo cannot hold)
over a fact about structure (which the repo holds better, and will change without
updating the note).
