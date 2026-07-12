# references — testing-discipline

Author-only memory-jog for what this skill was built on. Not part of the skill; leave out
when copying the skill into a project.

## Sources

- **Addy Osmani's `test-driven-development` SKILL.md**
  (https://github.com/addyosmani/agent-skills/blob/main/skills/test-driven-development/SKILL.md)
  — used as the backbone for the test-first workflow, the Prove-It (failing-test-first) bug
  pattern, the test-shape guidance (unit/integration/e2e), "state over interactions",
  "prefer real implementations over mocks", DAMP-in-tests, and the rationalizations table.
  Adapted, not copied: generalized off its TypeScript/`npm test`/Chrome-DevTools-MCP
  specifics into stack-agnostic pseudocode, and dropped the browser-testing and
  subagent sections as out of scope for this repo.

- **Mewgenics source-code review (YouTube talk, Tyler / Edmund McMillen), captured in
  scratch `tmp.md`.** Origin of the **Fuzz & Property Testing** section: no unit tests,
  instead a headless harness that runs the game with randomized cats/levels as fast as
  possible overnight; every crashing/soft-locking run's random seed is saved for
  deterministic replay and morning triage. Also the source of two framing points —
  fuzzing finds breakage not balance (win-rate metrics from random play are noise), and
  the crash-vs-"should-behave-differently" triage distinction.

## Related repo content

- `code-smell-audit` §9 "Order-dependent behavior over an unordered collection" — the
  determinism prerequisite for fuzzing cross-links to it; both trace to the same Mewgenics
  point about sorted/deterministic iteration order.
