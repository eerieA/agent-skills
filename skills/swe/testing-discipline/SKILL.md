---
name: testing-discipline
description: >
  Language- and framework-agnostic testing discipline for writing and reviewing
  tests. Covers test-first / prove-it-with-a-failing-test workflow, what makes a
  test good (state over interactions, real implementations over mocks, descriptive
  names, isolation), how to size and shape a suite (unit / integration / e2e), and
  fuzz / property testing for combinatorial systems whose input space is too large
  to enumerate by hand. Use when implementing new behavior, fixing a bug, deciding
  what kind of test to write, reviewing a test suite, or testing a system with a
  huge or combinatorial input space (parsers, game/simulation logic, state
  machines, schedulers).
metadata:
  domain: swe
  scope: implementation, review
  output-format: code
---

# Testing Discipline

Language- and framework-agnostic guidance for writing and reviewing tests. The
examples use generic pseudocode; apply them in whatever test framework the project
already uses. This skill is about *what* to test and *why a test earns its place* —
not about a specific runner's API.

## When to Use This Skill

- Implementing any new logic or behavior
- Fixing a bug (write the failing test first — the Prove-It pattern)
- Deciding what *kind* of test a change needs (unit / integration / e2e)
- Reviewing a test suite for gaps, flakiness, or over-mocking
- Testing a system whose input space is combinatorial and can't be enumerated by
  hand — parsers, game/simulation logic, state machines, schedulers, protocols
  (see **Fuzz & Property Testing**)

**When NOT to use:** pure config, docs, or static-content changes with no behavioral
impact.

## Core Principles

1. **A test proves behavior; "seems right" is not done.** The test is the specification.
2. **Test the observable outcome, not the internals.** Assert on what the code produces
   (return value, resulting state, emitted effect), not on which internal methods were
   called. Interaction-based tests break on refactors that changed nothing a user sees.
3. **Prefer real code over test doubles.** The more real implementation a test exercises,
   the more real bugs it can catch. Reach for a double only at boundaries that are slow,
   non-deterministic, or have uncontrollable side effects (network, clock, email).
4. **Isolate.** Each test sets up and tears down its own state. Tests must pass in any
   order and individually — order-dependence is a bug in the suite.
5. **Make failure reproducible.** A test (or a fuzz run) that fails must fail the same
   way when re-run. Pin clocks, seed randomness, control external inputs.

## Test-First Workflow

Write the test before the code that satisfies it. A test that passes the moment you
write it has proven nothing.

```
RED  — write a test that fails for the right reason
GREEN — write the minimum code to make it pass (don't over-build)
REFACTOR — clean up with the test green; re-run after each change
```

### The Prove-It Pattern (bug fixes)

When a bug is reported, **do not start with the fix.** Start with a test that reproduces
it and fails against the current code. Then fix. Then confirm the test passes and the rest
of the suite still does.

```
reproduce the bug in a test  →  test FAILS (bug confirmed)
implement the fix            →  test PASSES (fix proven)
run the full suite           →  no regressions
```

A reproduction test written *before* the fix tests behavior; one written after tends to
just enshrine whatever the fix happened to do.

## What Kind of Test

Invest effort by shape: most tests small and fast, progressively fewer as they get
broader and slower.

| Kind | Scope | Speed | Use for |
|------|-------|-------|---------|
| Unit | Pure logic, no I/O | ms | Functions, transforms, decision logic |
| Integration | Crosses a boundary (DB, API, filesystem) | s | Component interactions, contracts |
| End-to-end | Full flow, real environment | min | Critical user paths only — keep few |

Decision guide:

- Pure logic, no side effects → **unit**
- Crosses a boundary (API, DB, filesystem) → **integration**
- Critical flow that must work start-to-finish → **e2e**, reserved for the few paths
  that genuinely warrant the cost

If a change breaks and no test caught it, that's a missing test — not the refactor's
fault. Cover what you care about keeping.

## Writing Good Tests

- **State over interactions.** Assert the outcome, not the call sequence (see principle 2).
- **Readable over DRY.** In tests, a little duplication that makes each test tell its own
  complete story beats shared helpers that force the reader to trace indirection. Each test
  should read like a small specification.
- **Arrange–Act–Assert.** Set up, perform the one action under test, assert the outcome.
- **One concept per test.** Separate tests for separate behaviors, so a failure names the
  behavior that broke instead of hiding three checks in one.
- **Descriptive names.** The name should read like a claim about behavior — "sets status
  to completed and records timestamp", not "works" / "test 3".

### Anti-patterns to flag in review

| Anti-pattern | Problem | Fix |
|---|---|---|
| Testing internal structure | Breaks on refactors that changed no behavior | Assert inputs → outputs |
| Flaky / order-dependent tests | Erode trust in the whole suite | Deterministic assertions; isolate state |
| Testing framework/library code | Wasted effort on third-party behavior | Test only your code |
| Snapshot abuse | Huge snapshots nobody reviews, break on any change | Small, reviewed snapshots only |
| Mocking everything | Green tests, broken production | Prefer real > fake > stub > mock; mock only at hard boundaries |

## Fuzz & Property Testing

Example-based tests check the cases you thought of. Some systems have an input space far
too large to enumerate that way — parsers, serializers, game/simulation logic, state
machines, schedulers, anything where many features combine and interact. For those,
**generate** inputs instead of listing them, and let volume find the case you'd never
have written by hand.

Two related techniques:

- **Property testing** — assert an *invariant* that must hold for all inputs, then let the
  framework generate many inputs and try to break it. Classic invariants: round-trips
  (`decode(encode(x)) == x`), "never crashes / never panics", "output stays within bounds",
  "result is independent of input order" (see below).
- **Fuzzing** — drive the whole system with randomized inputs/sequences and watch for
  crashes, hangs, soft-locks, or invariant violations. A headless harness that runs the
  system as fast as possible, overnight, exploring random combinations, will surface
  edge-case interactions no hand-written suite covers.

### The rule that makes fuzzing usable: reproducible seeds

A random failure you can't reproduce is nearly worthless. **Every generated run must be
regeneratable from a saved seed.** When a run crashes or violates an invariant, record the
seed; then re-running with that seed replays the exact failing scenario for debugging.

```
seed = pick_seed()          # from an entropy source, ONCE per run
log(seed)                   # ← the one thing you must not lose
inputs = generate(seed)     # deterministic given the seed
result = run(system, inputs)
if result.failed:
    save_failing_seed(seed) # collect these; triage the list later
```

A practical loop: run the harness continuously (e.g. overnight), append each failing seed
to a list, and in the morning replay each one deterministically to debug. Optimizing the
harness to run *faster* directly buys more coverage — more scenarios explored per hour.

### Triage: crash vs. disagreement

Not every finding is a bug. Separate:

- **Hard failures** — crashes, hangs, soft-locks, violated invariants. These are real; fix
  them.
- **"Should behave differently" reports** — the system did something coherent that someone
  dislikes. That's a design question, not a defect. Don't let the fuzzer's noise get filed
  as bugs.

### What fuzzing does *not* do

Fuzzing finds *breakage*, not *balance* or *quality*. It tells you the system didn't crash
on a wild input; it can't tell you the behavior was good. Metrics harvested from random
play (win rates, throughput on nonsense inputs) are mostly noise — occasionally useful as a
smell test ("this option has a 100% win rate — why?"), never as ground truth.

### Determinism is a prerequisite

Fuzzing and property testing only pay off if the system is deterministic given its inputs
and seed. Hidden nondeterminism — unpinned clocks, unordered iteration that affects output,
unseeded randomness inside the system under test — makes failures irreproducible and
invariants flaky. That same order-dependence is a code smell in its own right; see the
`code-smell-audit` skill, category "Order-dependent behavior over an unordered collection".

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "I'll write tests after it works" | You won't — and after-the-fact tests test the implementation, not the behavior |
| "Too simple to test" | Simple code grows complicated; the test documents the intended behavior |
| "I tested it manually" | Manual testing doesn't persist; the next change breaks it silently |
| "It's just a prototype" | Prototypes become production; test debt compounds |
| "Let me run the suite again to be sure" | After a clean run on unchanged code, re-running adds no information — run again only after a change that could affect the result |

## Verification Checklist

- [ ] Every new behavior has a corresponding test
- [ ] Bug fixes include a reproduction test that failed before the fix
- [ ] Tests assert observable outcomes, not internal call sequences
- [ ] Tests pass individually and in any order (isolated state)
- [ ] Test names describe the behavior being verified
- [ ] For combinatorial systems: a fuzz/property harness exists and failing seeds are saved
- [ ] No tests were skipped or disabled to make the suite pass
