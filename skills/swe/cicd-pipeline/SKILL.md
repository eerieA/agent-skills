---
name: cicd-pipeline
description: >
  Platform-agnostic CI/CD deployment pipeline design and review. Covers how to
  stage a pipeline (build → test → promote → deploy → verify), where approval and
  metric gates belong, choosing a rollout strategy (rolling / blue-green / canary /
  feature flag), making rollback safe (including backward-compatible database
  migrations), writing health checks that don't lie, and the build-once-promote-the
  -same-artifact discipline. Use when designing a pipeline for a new service,
  adding gates or environments, choosing or debugging a rollout strategy, hardening
  rollback, or reviewing an existing pipeline for reliability gaps. Applies to any
  runner (GitHub Actions, GitLab CI, Jenkins, Azure Pipelines) and any target
  (Kubernetes, ECS, VMs, serverless).
metadata:
  domain: swe
  scope: design, review
  output-format: config
---

# Pipeline Design

Platform-agnostic guidance for designing and reviewing CI/CD deployment pipelines.
This skill is about *what a pipeline should do and why* — stage order, where gates
belong, which rollout strategy fits, how to make rollback and health checks
trustworthy. It is **not** a syntax reference for any one runner. Principles are
stated in prose and pseudocode; concrete snippets (GitHub Actions, Kubernetes, Argo
Rollouts, etc.) appear only as *one illustration* of a principle — translate them to
whatever runner and target the project actually uses.

## When to Use This Skill

- Designing a pipeline for a new service or a platform migration
- Adding an environment (a new staging tier) or a gate (approval, security, metric)
- Choosing a rollout strategy, or debugging one that stalls or fails silently
- Hardening rollback — especially when a release includes a database migration
- Reviewing an existing pipeline config for reliability gaps (use the checklist at
  the end)

**When NOT to use:** picking the exact YAML key for a runner feature (read that
runner's docs), or app-level test design (see the `testing-discipline` skill — this
skill decides *where tests run in the pipeline*, not what makes a test good).

## The Core Discipline: Build Once, Promote the Same Artifact

The single most important pipeline invariant: **build the artifact once, then
promote that exact artifact — unchanged — through every environment.** Do not
rebuild for staging and rebuild again for production. A rebuild can pull a different
base image, a floating dependency, or a different build-time flag, so "the thing you
tested" and "the thing you shipped" are no longer the same bytes — and the
difference surfaces only in production.

- Build produces an immutable, content-addressed artifact (an image digest, a
  versioned package). Everything downstream references *that digest*, never a
  rebuild and never a mutable tag like `latest`.
- Environment differences (URLs, replica counts, secrets) live in *config injected
  at deploy time*, not in the artifact.

The tell that this is violated: a `docker build` (or equivalent) step inside the
staging job *and* inside the production job. There should be one build, and the
later jobs consume its output.

## Standard Stage Flow

Most pipelines are a variation on this sequence. Name the stages after their job so
a reader sees the algorithm:

```
Source → Build → Test → Deploy(staging) → Integration → Gate → Deploy(prod) → Verify → (Rollback on failure)
```

1. **Source** — checkout, resolve dependencies
2. **Build** — compile, package, containerize, *sign* the artifact (once — see above)
3. **Test** — unit + integration + security scans (SAST/SCA); the cheap, fast checks
4. **Deploy (staging)** — deploy the artifact to a prod-like environment, run smoke tests
5. **Integration** — E2E, contract tests, performance baselines against staging
6. **Gate** — manual approval and/or an automated metric gate (see below)
7. **Deploy (production)** — using the chosen rollout strategy
8. **Verify** — *deep* health checks and synthetic monitoring against production
9. **Rollback** — automatic, triggered by a failure signal from Verify

**Fail fast, order by cost.** Run the cheap, high-signal checks first (lint, unit
tests) and the slow, expensive ones later (E2E, security scans, staging deploy). A
lint failure should not wait behind a ten-minute integration suite. Run independent
jobs in parallel; only serialize where there is a real dependency.

## Gates: Where to Stop and Check

A gate is a deliberate pause between stages. There are two kinds, and mixing them up
is a common design error.

**Manual approval gate** — a human authorizes promotion. Use it for the
production boundary where judgment or compliance sign-off is required. The failure
mode to avoid: a gate configured to wait for an approver who is never notified, or a
required-reviewer list pointing at no one — the pipeline then hangs forever with no
signal. Every manual gate needs a real, notified approver and a timeout.

**Automated metric gate** — the pipeline queries a real signal (error rate,
latency, saturation) and blocks promotion if it crosses a threshold. This is what
makes canary promotion trustworthy. The critical detail: **decide what happens when
the metric query returns *no data*.** "No data" is not "healthy." A gate that treats
missing/inconclusive results as pass will happily promote a broken release whose
metrics stopped reporting; a gate with no inconclusive-limit will hang forever
waiting for data that never comes. Set an explicit inconclusive limit that *fails*
(or alerts) rather than silently passing or hanging.

> _e.g. (Argo Rollouts) — the `inconclusiveLimit` is the safety valve; without it a
> metric that stops reporting stalls the rollout indefinitely:_
> ```yaml
> metrics:
> - name: error-rate
>   successCondition: "result[0] >= 0.95"
>   failureCondition: "result[0] < 0.90"
>   inconclusiveLimit: 3   # after 3 no-data results, fail — don't hang, don't pass
> ```

## Choosing a Rollout Strategy

Pick by *blast radius tolerance*, *rollback speed needed*, and *cost*. The decision
is about risk, not fashion.

| Strategy | Downtime | Rollback | Cost | Best for |
|---|---|---|---|---|
| **Rolling** | None | Minutes (roll back revision by revision) | None | Most stateless services — the sane default |
| **Blue-Green** | None | Instant (flip traffic back) | ~2× infra during switchover | High-risk releases, long warm-up, or DB-migration releases you may need to abandon fast |
| **Canary** | None | Instant (metric gate aborts) | Minimal | High-traffic services where real-user metrics can validate a small slice first |
| **Recreate** | Yes | Fast | None | Dev/test, batch jobs, anything where a blip is fine |
| **Feature flag** | None | Instant (per segment, no redeploy) | None | Decoupling *release* from *deploy*; gradual exposure and A/B |

Decision rules:

- **Default to rolling** for a stateless service. Don't reach for canary/blue-green
  complexity without a reason (high traffic, high risk, slow warm-up).
- **Canary needs a metric gate to mean anything.** A canary that shifts traffic on a
  timer without checking real metrics is just a slow rolling deploy — you've paid the
  complexity and gotten none of the safety. If you can't measure the canary, don't
  run one.
- **Feature flags are a different axis, not a competitor.** They let you *deploy*
  code dark and *release* it later by flipping a flag — useful on top of any of the
  deploy strategies above, and the fastest per-user rollback.
- **Blue-green earns its 2× cost** when instant, whole-version rollback matters more
  than infra spend — notably around risky migrations (below).

## Rollback Must Be Real — and Migrations Are the Trap

"We can roll back" is only true if you've designed for it. The stateless case is
easy: keep the previous artifact revision and re-point to it. The hard case, and the
one that turns a routine rollback into an outage, is **database migrations.**

If a release applies a destructive or backward-incompatible schema change and then
you roll the *code* back, the old code now runs against a schema it doesn't
understand — a self-inflicted outage on top of whatever you were rolling back from.

The discipline:

- **Make migrations backward-compatible (additive-only) for at least one release
  cycle.** Add columns/tables nullable; the old code must keep working against the
  new schema. Never `DROP COLUMN` / `ALTER ... NOT NULL` / rename in the same release
  that first needs the change.
- **Retire the old shape only after the old code is gone from every environment** —
  a later, separate release.
- **Version the undo alongside the migration** so rollback is a known, tested step,
  not an improvisation.

  ```
  migrations/2026_03_15_add_nullable_column.sql        (forward)
  migrations/2026_03_15_add_nullable_column.undo.sql   (backward)
  ```

- **Automate rollback on a failure signal.** The Verify stage's health/metric result
  should *trigger* the rollback, not just report red and wait for a human at 3am.

  > _e.g. — the rollback fires from the verify step's failure, not from a pager:_
  > ```yaml
  > - name: Verify
  >   id: health
  >   run: ./verify-deployment.sh https://app.example.com
  > - name: Rollback on failure
  >   if: failure()
  >   run: <re-point to previous revision>
  > ```

## Health Checks That Don't Lie

A pipeline is only as trustworthy as the signal it gates on. The classic failure:
the pipeline health check hits a **shallow** endpoint (`/ping`) that returns 200 as
long as the process is up — even when the database, cache, or queue it depends on is
unreachable. The gate goes green; production is broken.

- **Gate on a *deep* readiness check** that actually exercises the critical
  dependencies (DB connection, cache, downstream queue) and returns unhealthy if any
  are down. Shallow liveness (`is the process alive?`) and deep readiness (`can it
  actually serve?`) are different questions — gate promotion on the second.
- **Verify with retries and a bounded timeout**, then treat exhaustion as failure
  (which triggers rollback). Retrying forever is just hanging with extra steps.

> _e.g. — a readiness endpoint that reports the truth about its dependencies:_
> ```python
> @app.get("/health/ready")
> async def readiness():
>     checks = {"db": await check_db(), "cache": await check_cache(), "queue": await check_queue()}
>     ok = all(checks.values())
>     return JSONResponse({"status": "ok" if ok else "degraded", "checks": checks},
>                         status_code=200 if ok else 503)
> ```

## Cross-cutting practices

- **Secrets come from a secret store** (Vault, cloud secret manager, the runner's
  encrypted secrets) — never hardcoded in pipeline config or baked into the artifact.
- **Idempotent deploys** — re-running a deploy produces the same result; a retried
  job must not corrupt state.
- **Environment parity** — keep staging as close to production as budget allows, or
  its green result means little.
- **Cache the slow, stable layers** (dependency installs, base build layers), not the
  source layer — order build steps so a source change doesn't bust the dependency
  cache. (This is the same "order matters" discipline as `code-smell-audit` §10 on
  duplicated sources of truth: one source, derived downstream.)
- **Annotate deployments** — emit a deploy marker to your monitoring tool so a
  metric change can be correlated to the release that caused it.
- **Track the DORA signals** the pipeline is uniquely positioned to measure:
  deployment frequency, lead time (commit → prod), change-failure rate, and mean time
  to recovery. They tell you whether the pipeline is actually helping.

## Design-Review Checklist

When reviewing an existing pipeline, walk these and flag each gap. Order roughly by
severity.

1. **Rebuild between environments** (High) — is the artifact built once and promoted,
   or rebuilt per environment? A per-environment rebuild breaks the "tested = shipped"
   guarantee.
2. **Shallow health gate** (High) — does promotion gate on a deep readiness check, or
   on a `/ping` that returns 200 while dependencies are down?
3. **Unsafe migration + rollback** (High) — can the code roll back against the new
   schema? Are migrations additive-only, with a versioned undo? Or does rollback
   guarantee a schema/code mismatch?
4. **No-data metric gate** (High) — does the automated gate treat "no data" or
   "inconclusive" as pass (silent bad promote) or as a hang (no inconclusive limit)?
5. **Rollback is manual-only** (Medium) — does a failed verify *trigger* rollback, or
   just turn red and wait for a human?
6. **Hanging approval gate** (Medium) — does every manual gate have a real, notified
   approver and a timeout, or can it wait forever on no one?
7. **Canary without a metric gate** (Medium) — is the canary validated by real
   signals, or is it a timed traffic shift dressed up as safety?
8. **Secrets in config** (High) — any secret hardcoded in pipeline files or baked into
   the artifact instead of pulled from a secret store?
9. **Slow-before-fast ordering** (Low) — do cheap checks (lint, unit) run before slow
   ones (E2E, scans), or does a lint typo wait behind a ten-minute suite?
10. **Mutable tags / `latest` in prod** (Medium) — is production pinned to an
    immutable digest/version, or to a tag that can move under it?

Present findings as a table (finding · severity · what goes wrong · suggested fix),
then fix only what the user approves — matching the existing config's style.
