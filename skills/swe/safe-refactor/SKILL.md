---
name: safe-refactor
description: >
  Language- and framework-agnostic discipline for refactoring — restructuring
  existing code to improve its design without changing observable behavior.
  Covers the safety loop (small steps, tests green after each, commit rhythm),
  when NOT to refactor, and a catalog of concrete refactoring operations (extract
  function, inline, introduce parameter object, replace conditional with
  polymorphism, guard clauses, split module, and more) stated as mechanical
  transformations. Use when asked to "refactor", "clean up", "restructure",
  "simplify", or "make this easier to change" — and when adding a feature is hard
  because of the current structure. Self-contained; composes with a code-smell or
  testing skill if the project has one, but needs neither.
metadata:
  domain: swe
  scope: implementation
  output-format: code
---

# Safe Refactor

Refactoring is changing the *structure* of code without changing what it *does*.
The observable behavior — return values, resulting state, emitted effects, public
API — is identical before and after. If behavior changes, it is not a refactor; it
is a rewrite or a feature, and it carries different risks and needs different review.

This skill is language- and framework-agnostic. Examples are short pseudocode; apply
them in whatever language the project uses, matching the existing style exactly.

## When to Use This Skill

- The user asks to "refactor", "clean up", "restructure", "simplify", or "make this
  easier to change"
- Adding a feature is hard because the current structure fights you
- Code was just made to work and now needs to be made clear (the REFACTOR step of a
  test-first cycle)
- A structural problem has been identified (long function, duplication, feature envy)
  and you are about to fix it

**When NOT to use this skill — do not refactor when:**

- **There are no tests and you can't add them first.** Without a way to prove behavior
  is preserved, you are editing blind, not refactoring. Add characterization tests
  first (see below), or stop.
- **The code works, is stable, and won't change again.** Restructuring it spends risk
  for no return. "It offends me" is not a reason.
- **You are under deadline pressure on a feature.** Don't mix refactoring into a
  feature change — you lose the ability to tell which change broke something.
- **You can't state the concrete improvement.** "Cleaner" is not a goal. Name it:
  "so the pricing rule lives in one place", "so this function fits on a screen".

## The Cardinal Rule: Separate the Two Hats

At any moment you are either **adding behavior** or **refactoring** — never both. Kent
Beck's two hats: when refactoring, you do not add functionality or fix bugs; when
adding behavior, you do not restructure. Switching hats mid-edit is how a "small
cleanup" ships a regression.

If you notice a bug while refactoring, note it and finish (or abandon) the refactor
first — then fix the bug as its own change, with its own test written to reproduce it
before the fix.

## The Safety Loop

Tests are what make a refactor *safe* rather than *hopeful*. The loop:

```
0. GREEN BASELINE — full suite passes before you touch anything. Commit.
1. ONE STEP       — apply a single named refactoring (see catalog). Small.
2. RUN TESTS      — still green? If red, you changed behavior — undo, don't debug forward.
3. COMMIT         — each green step is a safe point you can return to.
4. REPEAT         — next small step, until the structure is where you want it.
```

Rules that make the loop work:

- **Small steps.** Each step should be reversible by one undo and independently green.
  A big-bang restructure that's red for an hour is not a refactor — it's a gamble.
- **Green after every step, not just at the end.** The point is to never be far from a
  known-good state.
- **Red means undo, not debug.** If a step turns the suite red, the refactor changed
  behavior. Revert that one step and take a smaller one — don't try to patch forward.
- **Commit at every green step.** Frequent commits (or a branch you squash later) give
  you a bisectable trail and a cheap escape hatch.
- **Automated tools are safer than hand-edits.** Prefer the IDE/language-server refactor
  (rename symbol, extract function, move) over manual find-and-replace — it updates all
  references and won't typo a call site.

### No tests yet? Characterize first.

If the code you must refactor has no tests, you cannot yet refactor it safely. Pin its
*current* behavior — including quirks — with **characterization tests**: feed it inputs,
record whatever it actually outputs, and assert that. You are not judging whether the
behavior is correct; you are nailing it down so the refactor can't change it silently.
Once behavior is pinned, enter the safety loop.

## Refactoring Catalog

Each entry is a mechanical transformation with a name. Naming the move keeps steps small
and reviewable — "I'm doing an Extract Function here" is a step; "cleaning this up" is not.
Detecting *which* smell warrants which move is the job of `code-smell-audit`; this catalog
is the *how*.

### Composing / decomposing functions

- **Extract Function** — pull a coherent fragment into its own named function; the name
  documents intent that a comment used to. The first and most common move.
  ```
  # before
  total = base
  total = total - base * discountRate   # apply discount
  total = total + total * taxRate       # apply tax
  # after
  total = applyTax(applyDiscount(base, discountRate), taxRate)
  ```
- **Inline Function** — the inverse. When a function's body is as clear as its name and
  the indirection earns nothing, fold it back into the caller.
- **Extract Variable** — give a sub-expression an explaining name.
  ```
  # before:  if (order.total > 100 && order.items.length > 0 && !order.isGift)
  # after:
  eligibleForFreeShipping = order.total > 100 && order.items.length > 0 && !order.isGift
  if (eligibleForFreeShipping) ...
  ```
- **Inline Variable** — remove a name that says no more than the expression it holds.

### Simplifying conditionals

- **Guard Clauses (replace nested conditional)** — handle edge cases with early returns
  so the main path un-nests to the left margin.
  ```
  # before: if (a) { if (b) { if (c) { work() } } }
  # after:
  if (!a) return
  if (!b) return
  if (!c) return
  work()
  ```
- **Decompose Conditional** — extract the test, the then-branch, and the else-branch into
  named functions (`isSummerRate(date)`, `summerCharge(...)`, `winterCharge(...)`).
- **Consolidate Conditional** — combine several checks that yield the same result into one
  named test.
- **Replace Conditional with Polymorphism** — when a `switch`/`if` on a type code recurs in
  several places, give each variant a type and let dispatch replace the branching. Reach
  for this only when the branching is *repeated*; a single local switch is fine.

### Data and parameters

- **Introduce Parameter Object** — replace a long parameter list (or a recurring clump of
  arguments passed together) with one object.
  ```
  # before: createUser(email, name, age, street, city, country, phone)
  # after:  createUser(userDetails)
  ```
- **Replace Magic Value with Named Constant** — swap an unexplained literal for a named
  constant declared once.
- **Encapsulate Field / Record** — route access to a piece of data through functions so
  its representation can change in one place.

### Moving things

- **Move Function / Field** — relocate a function to the module or type whose data it
  mostly uses (the fix for feature envy: put the behavior next to the data it acts on).
- **Extract Module / Class** — when one unit has grown two responsibilities, split it so
  each has a single reason to change. The structural fix for a god object / large module.
- **Combine Functions into a Module** — the inverse; gather scattered functions that
  operate on the same data into one cohesive unit.
- **Rename** — a first-class refactoring, not a cosmetic afterthought. A precise name
  removes the need for a comment. Use the tool-assisted rename so every reference updates.

### Removing

- **Remove Dead Code** — delete unreachable code, unused parameters, and commented-out
  blocks. Version control remembers it; the reader shouldn't have to.

## Design Patterns: Use With Restraint

Patterns (Strategy, Factory, Chain of Responsibility, Template Method…) are legitimate
refactoring *targets*, but a pattern is a cost — indirection a future reader must learn.
Introduce one only when the duplication or the branching it removes is real and repeated.
Refactoring *toward* a pattern once you feel the pain beats designing it in up front.
Adding a pattern to code that has one call site is not refactoring; it's over-engineering.

## Relationship to Other Skills

This skill is self-sufficient — it does not require any other skill to be present. The
references below are optional: when a project *also* uses the named skill, the two compose;
when it doesn't, ignore the reference and proceed with this skill alone.

- **`code-smell-audit`** (if the project uses it) — *detects* what is wrong or risky (long
  functions, duplication, feature envy, silent fallbacks, order-dependence) and helps decide
  *what* to change and *whether it's worth it*. This skill is *how* to change it safely:
  audit finds, refactor transforms. Without it, judge candidates using the "When NOT to use"
  criteria above.
- **`testing-discipline`** (if the project uses it) — goes deeper on shaping the tests the
  safety loop depends on and the characterization-test technique. This skill already states
  inline everything the safety loop needs, so the reference is for extra depth, not a
  prerequisite.

## Verification Checklist

- [ ] Behavior is unchanged — same observable outputs, state, effects, and public API
- [ ] Tests existed (or were added as characterization tests) *before* refactoring began
- [ ] The full suite is green, and was green after every step — not just at the end
- [ ] No behavior change and no bug fix rode along inside the refactor (two hats kept separate)
- [ ] Each step is a named refactoring operation, committed while green
- [ ] The concrete improvement can be stated in one sentence
- [ ] No pattern or abstraction was introduced without repeated, real duplication to justify it
