# Keep rules — what must survive compaction

The over-correction guard. Consult this **before** writing any finding; it has veto
power over every pattern in `patterns.md`.

The failure mode of this skill is a tidy comment block that no longer contains the one
sentence that would have stopped the next bug. That failure is invisible at review time
— the diff looks like an improvement — and expensive later. Bias accordingly: **when a
cut is arguable, don't.**

## The recovery test

The only test that matters. For each candidate sentence:

> Given the code beside it, the sentence before it, the identifiers, and the type
> signature — would a competent reader who lacked this sentence be missing anything?

- **Missing something → fact → keep**, however long the block gets.
- **Missing nothing → derivable → cut.**

Two failure modes in applying it:

- **Over-crediting the reader.** "A competent reader knows the API classifies from the
  border pair" — no, they don't; that's in another repo. Recoverable means recoverable
  *from what is in front of them*, not from expertise you happen to have.
- **Under-crediting the reader.** "Returns null when the input is empty" above
  `if (!candidate) return null` credits them with nothing.

## Always keep

**Facts about systems outside this file.** Another repo's behaviour, an API's actual
contract as opposed to its documented one, a NetBox field's semantics, a library's
undocumented quirk. The reader cannot grep for these from here, and there is no second
copy. This is the single largest category of wrongly-cut prose.

**The why behind a non-obvious choice.** Why this order, why this type, why not the
obvious alternative. Code records *what*; nothing except the comment records *why*, and
the absence reads as arbitrariness — which invites "cleanup" that reintroduces the bug.

**Guards against plausible-but-wrong changes.** Any sentence of the form "do not X, it
looks right but Y". These have negative length in expectation: they cost lines now and
save a debugging session later. Never cut one for length. If it is long because the
wrong change is subtle, it is long for the right reason.

**Gotchas that still bite.** Sharp edges a reader will hit. The test is whether the edge
is still there — a gotcha about removed code is history and goes; a live one stays.

**Non-derivable constraints.** "Must run before X", "callers assume sorted", "not
thread-safe", "the list is a snapshot, so this races". Invariants a caller cannot see
from the signature.

**Measured numbers with their conditions.** "3–21 s on dev with 400 buildings." The
number is only meaningful with the condition; cutting the condition leaves a figure that
will be misapplied. Either keep both or cut both.

**Load-bearing precision.** `name__ie` is case-insensitive *exact*, not case-insensitive
*contains*. Compressing to "case-insensitive" loses the half that decides whether the
client-side check is sound.

**One worked example, where the rule is abstract.** A single `"VN-1" vs "vn-1"` does more
than three sentences of explanation. Examples read as padding and are usually the densest
lines in the block.

## Keep, with judgment

**Structural signposts in long documents.** In a 400-line doc, "this section covers X"
is navigation, not narration. In a 20-line one it is filler. Length of the *container*
decides.

**Deliberate redundancy across audiences.** A safety warning may legitimately appear in
both the runbook step and the overview, because the two are read by different people at
different times. Rare, real, and requires a stated reason — otherwise it is the
two-copies-that-drift problem.

**Restatement across a long gap.** If forty lines separate a fact from the code relying
on it, a short restatement at the point of use is cheaper than a scroll. Prefer moving
the fact.

## Never touch

**Code, identifiers, paths, commands, URLs, env vars, error strings.** Compaction works
on prose between these.

**Version numbers and dates inside a technical claim.** "Fixed in 0.1.14" as status is a
stamp and goes. "The 0.1.14 schema types it `String!`" is a fact about a specific
version and stays — the version *is* the claim.

**Quoted external text.** Someone else's error message, spec language, or comment. Quote
or cut whole; never silently paraphrase, and never compact inside quotation marks.

**Files another team owns.** Upstream specs, API contracts, other repos' docs. Report,
do not edit.

**Legal, licence, safety, and attribution text.** Not in scope at any length.

## Not evidence of bloat on its own

- **A long comment.** Length tracks how much non-obvious context exists. Some code needs
  twelve lines.
- **A comment longer than the code it describes.** A three-line function embodying a
  network-design ruling needs more explanation than code. Ratio is not a signal.
- **Repetition of a term.** Deliberate; the alternative is synonym rotation, which is
  worse. Do not "vary" a fixed term.
- **A list where prose would do.** Lists are scannable. Converting a list to a paragraph
  to save lines is a downgrade.
- **Emphasis, once.** One `⚠️` on the actual trap is doing its job. The tell is seven.
- **A cross-reference to another doc.** Pointers are how minimality and completeness
  coexist. Cutting them undoes the mechanism.
- **A sentence you personally find obvious.** You have the whole file in context and just
  read it. The reader arriving in eight months does not.

## Before applying any cut

Three checks:

1. **Where else does this fact live?** Nowhere → it is not a cut, it is a deletion.
2. **Would the next person to touch this line have needed it?** Unsure → keep.
3. **Am I cutting to make it shorter, or because it carries nothing?** Only the second is
   in scope. If the honest answer is "it's a bit long", stop.
