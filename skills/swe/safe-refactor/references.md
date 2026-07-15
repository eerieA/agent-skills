# references — safe-refactor

Author-only memory-jog for what this skill was built on. Not part of the skill; leave out
when copying the skill into a project.

## Sources

- **`refactor` SKILL.md** (github/awesome-copilot)
  (https://github.com/github/awesome-copilot/blob/main/skills/refactor/SKILL.md)
  — a primary backbone for the durable judgment: the "behavior is preserved / small steps /
  version control is your friend / tests are essential / one thing at a time" Golden Rules,
  the "When NOT to Refactor" guardrail, the safe-refactoring process (prepare → identify →
  refactor → verify), and the catalog of common operations. Adapted, not copied: its code
  examples were TypeScript/web-flavored (interfaces, `as const`, React-ish component
  extraction), so the durable moves were generalized into short language-neutral pseudocode
  and the code-smell catalog was dropped to avoid overlap with `code-smell-audit`.

- **`refactoring-specialist` subagent** (VoltAgent/awesome-claude-code-subagents)
  (https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/06-developer-experience/refactoring-specialist.md)
  — source of the detailed, small-step decomposition style and the breadth of the
  refactoring catalog (extract/inline, introduce parameter object, replace conditional with
  polymorphism, move function/field, extract module). Adapted, not copied: reframed from a
  "senior specialist" persona with metrics/communication-protocol scaffolding into plain
  procedural guidance, and its code-smell-detection list was deliberately left out because it
  overlaps `code-smell-audit`.

- **`refactor` slash-command skill** (claudedirectory.org)
  (https://www.claudedirectory.org/skills/refactor)
  — source of the no-fluff wording style and the tight categorization (structure /
  simplification / patterns) plus the "safety guarantees" framing (never change external
  behavior, run tests after each step, atomic commits, preserve public API). Its brevity set
  the tone for this skill's prose.

## Design decisions specific to this skill

- **Two hats (add-behavior vs. refactor, never both)** and **"red means undo, not debug"**
  were added beyond what the three sources spelled out — they are the load-bearing discipline
  that keeps a "cleanup" from shipping a regression.
- **Patterns with restraint** reframes the sources' design-pattern menus (Strategy, Chain of
  Responsibility, etc.) as a cost to introduce only under real, repeated duplication, rather
  than a catalog to apply.
- Kept **language-agnostic** and **standalone** on purpose: no framework-specific examples,
  and references to sibling skills are optional ("if the project uses it"), not prerequisites.
