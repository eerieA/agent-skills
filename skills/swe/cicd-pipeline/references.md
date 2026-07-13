# references — cicd-pipeline

Author-only memory-jog for what this skill was built on. Not part of the skill; leave out
when copying the skill into a project.

## Sources

- **`deployment-pipeline-design` SKILL.md + `references/details.md`** (wshobson/agents)
  (https://github.com/wshobson/agents/blob/main/plugins/cicd-automation/skills/deployment-pipeline-design)
  — the primary backbone. Adapted, not copied: took the durable design judgment
  (standard stage flow, manual vs. automated gates, the rollout decision table,
  build-once-promote, deep-vs-shallow health checks, backward-compatible migrations +
  versioned undo, automated-rollback-on-failure, DORA signals) and generalized it off
  the Kubernetes/Argo Rollouts/Prometheus specifics into platform-agnostic prose. Kept
  a few tool snippets (Argo `inconclusiveLimit`, a readiness endpoint, a GH-Actions
  `if: failure()` rollback) only as clearly-marked "e.g." illustrations of a principle.
  The most valuable transferable lessons came from its Troubleshooting section:
  health-check-lies (shallow /ping), canary-stall on no-data metrics, hanging approval
  gate with no reviewer, cache-bust ordering, and migration/rollback schema mismatch.

## Also reviewed (not used as backbone)

- **`jenkins-pipeline`** (aj-geddes/useful-ai-prompts) — Jenkinsfile declarative/scripted
  syntax reference. Rejected as the basis: tool-specific, ages fast, only helps on Jenkins.
- **`deployment-automation`** (aj-geddes/useful-ai-prompts) — Helm/Terraform/ArgoCD
  implementation + DO/DON'T lists. Mostly tool dumps; thin on durable judgment.
- **`devops-engineer`** (Jeffallan/claude-skills) — broad "senior DevOps persona" covering
  Docker, K8s, Terraform, CI/CD, incidents, platform eng. Too broad to adapt cleanly into
  one focused skill.

## Related repo content

- `testing-discipline` — that skill decides *what makes a test good*; this one decides
  *where tests run in the pipeline* (unit/scan early, E2E against staging, deep health at
  verify). Cross-referenced in the "When NOT to use" note.
- `code-smell-audit` §10 (duplicated source of truth) — cited in the caching note: one
  source, derived downstream; same "order matters / single source" discipline.
