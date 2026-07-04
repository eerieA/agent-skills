# UI & Interaction Guidelines

Adapted from [Vercel's Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines) (used with attribution). Most are framework-agnostic; some are React/Next.js-specific. The Copywriting section reflects Vercel's own brand voice — treat it as one example of a consistent voice, not a mandate, unless this project has adopted it deliberately.

## Interactions

- **Keyboard works everywhere.** All flows are keyboard-operable & follow the [WAI-ARIA Authoring Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/).
- **Clear focus.** Every focusable element shows a visible focus ring. Prefer `:focus-visible` over `:focus` to avoid distracting pointer users. Set `:focus-within` for grouped controls.
- **Manage focus.** Use focus traps, move & return focus according to the WAI-ARIA Patterns.
- **Match visual & hit targets.** Exception: if the visual target is < 24px, expand its hit target to ≥ 24px. On mobile, the minimum size is 44px.
- **Mobile input size.** `<input>` font size is ≥ 16px on mobile to prevent iOS Safari auto-zoom/pan on focus.
- **Respect zoom.** Never disable browser zoom.
- **Hydration-safe inputs.** Inputs must not lose focus or value after hydration.
- **Don't block paste.** Never disable paste in `<input>` or `<textarea>`.
- **Loading buttons.** Show a loading indicator & keep the original label.
- **Minimum loading-state duration.** If you show a spinner/skeleton, add a short show-delay (~150–300 ms) & a minimum visible time (~300–500 ms) to avoid flicker on fast responses. React's `<Suspense>` does this automatically.
- **URL as state.** Persist state in the URL so share, refresh, Back/Forward navigation work (e.g. [nuqs](https://nuqs.dev)).
- **Optimistic updates.** Update the UI immediately when success is likely; reconcile on server response. On failure, show an error & roll back or provide Undo. See `useOptimistic` in `modules/hooks-and-state.md`.
- **Ellipsis for further input & loading states.** Menu options that open a follow-up ("Rename…") & loading/processing states ("Loading…", "Saving…") end with an ellipsis.
- **Confirm destructive actions.** Require confirmation or provide Undo with a safe window.
- **Prevent double-tap zoom on controls.** Set `touch-action: manipulation`.
- **Design forgiving interactions.** Generous hit targets, clear affordances, predictable interactions.
- **Tooltip timing.** Delay the first tooltip in a group; subsequent peers have no delay.
- **Overscroll behavior.** Set `overscroll-behavior: contain` intentionally (e.g. in modals/drawers).
- **Scroll positions persist.** Back/Forward restores prior scroll.
- **Autofocus for speed.** On desktop screens with a single primary input, autofocus. Rarely autofocus on mobile — the keyboard opening can cause layout shift.
- **No dead zones.** If part of a control looks interactive, it should be interactive.
- **Deep-link everything.** Filters, tabs, pagination, expanded panels — anytime `useState` is used for view state that a user might want to share or return to.
- **Clean drag interactions.** Disable text selection & apply `inert` while an element is dragged.
- **Links are links.** Use `<a>` or `<Link>` for navigation so Cmd/Ctrl+Click, middle-click, right-click work. Never substitute `<button>` or `<div>`.
- **Announce async updates.** Use polite `aria-live` for toasts & inline validation.
- **Locale-aware keyboard shortcuts.** Internationalize shortcuts for non-QWERTY layouts; show platform-specific symbols.

## Animations

- **Honor `prefers-reduced-motion`.** Provide a reduced-motion variant.
- **Implementation preference.** CSS > Web Animations API > JS libraries. Avoid main-thread JS-driven animations when possible.
- **Compositor-friendly.** Prioritize `transform`/`opacity`; avoid properties that trigger reflow (`width`, `height`, `top`, `left`).
- **Necessity check.** Only animate when it clarifies cause & effect or adds deliberate delight.
- **Interruptible.** Animations are cancelable by user input.
- **Input-driven.** Avoid autoplay; animate in response to actions.
- **Correct transform origin.** Anchor motion to where it "physically" starts.
- **Never `transition: all`.** Explicitly list only the properties you intend to animate.
- **Cross-browser SVG transforms.** Apply transforms to `<g>` wrappers & set `transform-box: fill-box; transform-origin: center;`.

## Layout

- **Optical alignment.** Adjust ±1px when perception beats geometry.
- **Deliberate alignment.** Every element aligns to something intentionally — grid, baseline, edge, or optical center.
- **Balance contrast in lockups.** When text & icons sit side by side, adjust weight/size/spacing/color so they don't clash.
- **Responsive coverage.** Verify on mobile, laptop, & ultra-wide.
- **Respect safe areas.** Account for notches & insets with [safe-area variables](https://developer.mozilla.org/en-US/docs/Web/CSS/env).
- **No excessive scrollbars.** Only render useful scrollbars; fix overflow issues.
- **Let the browser size things.** Prefer flex/grid/intrinsic layout over measuring in JS.

## Content

- **Inline help first.** Prefer inline explanations; tooltips as a last resort.
- **Stable skeletons.** Skeletons mirror final content exactly to avoid layout shift.
- **Accurate page titles.** `<title>` reflects current context.
- **No dead ends.** Every screen offers a next step or recovery path.
- **All states designed.** Empty, sparse, dense, & error states.
- **Typographic quotes.** Curly quotes (" ") over straight quotes (").
- **Avoid widows/orphans.** Tidy rag & line breaks.
- **Tabular numbers for comparisons.** `font-variant-numeric: tabular-nums` or a monospace font.
- **Redundant status cues.** Don't rely on color alone; include text labels.
- **Icons have labels.** Convey the same meaning with text for non-sighted users.
- **Don't ship the schema.** Visual layouts may omit visible labels, but accessible names/labels still exist for assistive tech.
- **Use the ellipsis character.** `…` over three periods `...`.
- **Anchored headings.** Set `scroll-margin-top` for headers when linking to sections.
- **Resilient to user-generated content.** Layouts handle short, average, & very long content.
- **Locale-aware formats.** Dates, times, numbers, delimiters, & currencies match user locale.
- **Prefer language settings over location.** Detect language via `Accept-Language` & `navigator.languages`, not IP/GPS.
- **Shield verbatim content from translation.** Wrap brand names, product names, code tokens with `translate="no"`.
- **Accessible content.** Set accurate `aria-label`, hide decoration with `aria-hidden`, verify in the accessibility tree.
- **Icon-only buttons are named.** Provide a descriptive `aria-label`.
- **Semantics before ARIA.** Prefer native elements (`button`, `a`, `label`, `table`) before `aria-*`.
- **Headings & skip link.** Hierarchical `<h1–h6>` & a "Skip to content" link.
- **Non-breaking spaces for glued terms.** `10&nbsp;MB`, `⌘&nbsp;+&nbsp;K`.

## Forms

- **Enter submits.** When a text input is focused, Enter submits if it's the only control. If there are many controls, apply to the last control.
- **Textarea behavior.** In `<textarea>`, ⌘/⌃+Enter submits; Enter inserts a new line.
- **Labels everywhere.** Every control has a `<label>` or is associated with one.
- **Label activation.** Clicking a `<label>` focuses the associated control.
- **Submission rule.** Keep submit enabled until submission starts; then disable during the in-flight request, show a spinner, include an idempotency key.
- **Don't block typing.** Even numeric-only fields should allow any input & show validation feedback rather than blocking keystrokes.
- **Don't pre-disable submit.** Allow submitting incomplete forms to surface validation feedback.
- **No dead zones on controls.** Checkboxes & radios: label & control share a single generous hit target.
- **Error placement.** Show errors next to their fields; on submit, focus the first error.
- **Autocomplete & names.** Set `autocomplete` & meaningful `name` values to enable autofill.
- **Spellcheck selectively.** Disable for emails, codes, usernames.
- **Correct types & input modes.** Use the right `type` & `inputmode`.
- **Placeholders signal emptiness.** End with an ellipsis; set to an example value or pattern (e.g. `+1 (123) 456-7890`).
- **Unsaved changes.** Warn before navigation when data could be lost.
- **Password managers & 2FA.** Ensure compatibility & allow pasting one-time codes.
- **Don't trigger password managers for non-auth fields.** Avoid reserved names like "password" for unrelated inputs.
- **Text replacements & expansions.** Trim input values — some input methods add trailing whitespace.
- **Windows `<select>` background.** Explicitly set `background-color` & `color` to avoid dark-mode contrast bugs on Windows.

## Performance

- **Device/browser matrix.** Test iOS Low Power Mode & macOS Safari.
- **Measure reliably.** Disable extensions that add overhead or change runtime behavior.
- **Track re-renders.** Minimize & make re-renders fast — see `modules/performance.md`.
- **Throttle when profiling.** Test with CPU & network throttling.
- **Minimize layout work.** Batch reads/writes; avoid unnecessary reflows/repaints.
- **Network latency budgets.** `POST/PATCH/DELETE` complete in <500ms.
- **Keystroke cost.** Prefer uncontrolled inputs; make controlled loops cheap.
- **Large lists.** Virtualize — see `modules/performance.md`.
- **Preload wisely.** Preload only above-the-fold images; lazy-load the rest.
- **No image-caused CLS.** Set explicit image dimensions & reserve space.
- **Preconnect to origins.** `<link rel="preconnect">` for asset/CDN domains.
- **Preload fonts.** For critical text to avoid flash & layout shift.
- **Subset fonts.** Ship only the code points/scripts you use.
- **Don't use the main thread for expensive work.** Move long tasks to Web Workers.

## Design

- **Layered shadows.** Mimic ambient + direct light with at least two layers.
- **Crisp borders.** Combine borders & shadows; semi-transparent borders improve edge clarity.
- **Nested radii.** Child radius ≤ parent radius & concentric so curves align.
- **Hue consistency.** On non-neutral backgrounds, tint borders/shadows/text toward the same hue.
- **Accessible charts.** Use color-blind-friendly palettes.
- **Minimum contrast.** Prefer [APCA](https://apcacontrast.com/) over WCAG 2 for more accurate perceptual contrast.
- **Interactions increase contrast.** `:hover`, `:active`, `:focus` have more contrast than rest state.
- **Browser UI matches your background.** Set `<meta name="theme-color" content="#000000">`.
- **Set the appropriate color-scheme.** `color-scheme: dark` on `<html>` in dark themes so scrollbars & device UI get proper contrast.
- **Text anti-aliasing & transforms.** Prefer animating a wrapper instead of the text node when scaling; use `translateZ(0)` or `will-change: transform` if artifacts persist.
- **Avoid gradient banding.** Use background images instead of CSS masks fading to dark colors.

## Copywriting (Vercel's voice — adapt or drop per project)

- **Active voice.** "Install the CLI," not "The CLI will be installed."
- **Headings & buttons use Title Case** (Chicago style). Sentence case on marketing pages.
- **Be clear & concise.** Fewest words possible.
- **Action-oriented language.** "Install the CLI…," not "You will need the CLI…"
- **Keep nouns consistent.** Introduce as few unique terms as possible.
- **Write in second person.**
- **Use consistent placeholders.** Strings: `YOUR_API_TOKEN_HERE`. Numbers: `0123456789`.
- **Use numerals for counts.** "8 deployments," not "eight deployments."
- **Consistent currency formatting.** 0 or 2 decimal places, never mixed in the same context.
- **Separate numbers & units with a space.** `10 MB`, not `10MB`; use a non-breaking space.
- **Default to positive language.** Even for errors: "Something went wrong—try again or contact support," not "Your deployment failed."
- **Error messages guide the exit.** State what went wrong *and* how to fix it.
- **Avoid ambiguity.** "Save API Key," not "Continue."
