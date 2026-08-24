# Bloat pattern catalog

What each tier looks like in practice. Every example is real prose from this repo, cut
and kept as shown. Check each candidate against `craft/keep-rules.md` before flagging.

Tiers: **Derivable** · **Narration** · **Stamp** · **Flourish**. (The fifth tier, Fact,
has no entries here — it is what survives.)

---

## Derivable

The reader reconstructs it for free from a fact already given, the code below, or the
signature. True, well-written, and still costing more than it pays.

### Consequence restatement

The dominant pattern. State a fact, then state what the fact implies. The implication was
free the moment the fact landed.

```
// BEFORE
// the deployed schema types it `String!`. So `null` is a hard schema error, and omitting
// the key only works by relying on JSON.stringify dropping `undefined`. The explicit
// empty string matches the API's own default and doesn't depend on that.

// AFTER
// the deployed schema types it `String!`.
```

`String!` *means* null is an error. A reader who knows GraphQL got the whole second
sentence from the first; a reader who doesn't won't be helped by it either.

Recognizer: a sentence opening **So / Therefore / This means / Which is why / As a
result** whose content follows from the sentence before.

### Branch enumeration

Prose walking through the branches of the code immediately below.

```
// BEFORE
// Per-step "can advance?" gate. Step 1 needs a name + a valid family/handoff
// combination; Step 2 needs an owning border pair; Steps 3/4 are informational
// (always passable). Returns an error string to show, or null when the step is satisfied.

// AFTER
// Per-step "can advance?" gate. Returns an error string to show, or null when the step
// is satisfied.
```

The three `if` blocks below say it, in the same order, in less space. Keep the block's
*purpose* (what "gate" means, what the return value signifies); drop the walk-through.

### Signature narration

```
// BEFORE
// Returns a reason string when invalid, else null.
export function invalidCombinationReason(...): string | null

// AFTER
(nothing — the signature is the sentence)
```

Keep it only where the mapping is non-obvious: *which* of two strings, or a null that
means something other than "absent".

### Return-value gloss

```
// BEFORE
// Returns the colliding existing name — its exact casing is what makes the warning
// useful ("VN-1 exists" when the user typed "vn-1").

// AFTER
// Returns the colliding existing name, casing intact.
```

Borderline: the example earns its place if the casing subtlety is the whole point of the
function. Cut the *explanation* of the example, keep the example. If the block is already
long, cut both — the type plus the name carries it.

### Parenthetical cross-reference

```
// BEFORE
// The API's ConflictError stays the real gate (mapped by the wizard's
// triggerErrorMessage).

// AFTER
// The API's ConflictError stays the real gate.
```

A reader who needs the mapping greps for `ConflictError`. Everyone else pays a line.
Keep the pointer when it is genuinely hard to find — a different repo, an unobvious
filename, a dynamic dispatch.

### Negative-space clarification

Explaining what something is *not*, when nobody would have thought it was.

```
// BEFORE  VRF-Lite is greyed out because of a silent-substitution hazard, not a
//         missing form field.
// AFTER   VRF-Lite is greyed out because of a silent-substitution hazard.
```

Keep the negation only where the wrong reading is genuinely tempting — then it is a
guard, not a clarification, and `keep-rules.md` protects it.

### Duplicated rationale across files

The same mechanism explained in two files. Not compressible in place — **relocatable**.
Pick the owning file, leave that copy whole, replace the other with a pointer.

```
// BEFORE (eligibility.ts — 6 lines restating createVnForm.ts's explanation)
// ⚠️ THIS FILTER IS NOT FAMILY-AWARE. Since `family` never reaches the trigger
// (createVnForm.ts's toRequestInput) and the API classifies from the pair alone, a
// VRF-Lite request used to COMPLETE as an EVPN-A VN. That is why the VRF-Lite family
// is greyed out in Step 1 — see createVnForm.ts's familyOptions().

// AFTER
// EVPN-only in practice, and NOT family-aware — the VRF-Lite hazard this creates is why
// Step 1 greys the family out; see createVnForm.ts's familyOptions() for the mechanism.
```

The highest-value cut in the catalog: it removes a line count *and* a future
contradiction. See `keep-rules.md` → one owner per fact.

### Instance state duplicated from a ledger

Specific dev-environment inventory (names, ids, which pod) inside a code comment, when a
doc already carries it. The *rule* is a fact and stays; the *inventory* drifts on the next
re-seed and belongs where inventory is maintained.

Distinguish carefully from **facts about other systems**, which look similar and must be
kept. Test: would this change if someone re-seeded the dev database? Yes → instance state.
No → external fact, keep.

---

## Narration

Describes what the code plainly does, in prose, in the same order. Distinct from
derivable: nothing is being inferred, it is being transcribed.

```
// BEFORE  Home-pod options: normal-campus pods only, sorted by name.
// AFTER   Home-pod options: normal-campus pods only.
```

`.sort((a, b) => a.name.localeCompare(b.name))` is the next line.

Also narration: step-comments inside a function (`// Step 1: build the map`) — these are
a naming problem, not a comment problem. Extract the step into a function whose name says
what the comment said. That is a `safe-refactor` move; flag and hand off.

---

## Stamp

Dates, versions, verification receipts, progress, build status. The **claim** stays; the
**receipt** relocates to whichever ledger owns status.

```
// BEFORE  the deployed schema types it `String!` (verified by introspection 2026-07-29,
//         and in noat-api-evpn's `graphql/workflow/inputs.py`: ...)
// AFTER   the deployed schema types it `String!` (noat-api-evpn's
//         `graphql/workflow/inputs.py` has ...)
```

The citation is a fact — it tells the reader where to look. The date is a receipt: it
cannot be kept true, and a stale date makes a live claim look doubtful.

Also stamps: "live as of v0.1.14", "fixed upstream, not yet deployed", "currently
blocked", "TODO(2026-Q3)", upstream commit hashes.

**The exception**, and it is narrow: a note whose entire job is to mark scaffolding with
its removal trigger ("delete this shim when the API ships `podId`"). That is a
self-destruct instruction, not a status report.

---

## Flourish

### The closing verdict

```
// BEFORE  ... the user asked for one family and silently got another, with no error to
//         notice. Greying the option is what makes the wizard honest.
// AFTER   ... selecting VRF-Lite silently produced an EVPN-A VN, with no error to notice.
```

The preceding lines earned the conclusion. Stating it adds a sentence and a faint
self-congratulation.

### Emphasis inflation

Not a sentence-level cut — a **block-level** one. Seven CAPS spans in twelve lines:
`GREYED OUT`, `NOT`, `EVERY`, `COMPLETED`, `ALONE`, `HAS`, `IS`. Emphasis is positional;
when everything shouts, the one real footgun stops standing out.

Cut to the two or three marking actual traps — `DO NOT` on the dangerous change, `IS` on
the one settled fact among unsettled ones. Downcase the rest. Same for `⚠️`: one per
hazard, in the file that owns the hazard.

### Hedge stacking

"generally", "typically", "in most cases", "usually" layered on one claim. Keep at most
one, and only where the uncertainty is real and the reader must act differently because
of it. Otherwise state the claim.

### Restated preamble

A section opening by summarizing what the section is about, before saying it. In a short
doc, cut. In a long one, see `keep-rules.md` → structural signposts.

---

## Structural patterns

Above the sentence. **Do these first** — compacting prose inside a section you then
delete is wasted work, and the investment biases you toward keeping it.

### Prose → table

Parallel items sharing attributes. Four sentences of "X does A, taking B" become four
rows, stop drifting in phrasing, and become scannable.

### Merged sections

Two headings a reader cannot tell apart = one section split by accident. Merge, keep both
sets of facts.

### Deleted overview or conclusion

Both are derivable from the body. Cut the conclusion first — a conclusion is never
navigation, whereas an overview may be a genuine map in a long document.

### Split blocks that stay split

The inverse move, and the reason this skill is not "merge everything". Two comment blocks
answering *different* questions ("what does this filter do" / "don't widen it") should
stay separate even though merging looks tidier — only the first is worth reading when you
are just calling the function. Merging forces every reader through both.
