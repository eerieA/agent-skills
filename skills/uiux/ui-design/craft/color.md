# craft — color (building a palette that means something)

Consulted from **Step 1.5** when choosing or judging a palette. The main skill's
invariant is a floor: *off-black/off-white neutrals, at most one accent, WCAG AA
contrast on everything.* This file is how you make choices that are not just
*legal* but *good* — a palette that expresses the governing concept and feels
harmonious rather than assembled. Everything here operates **inside** the AA floor;
if a beautiful pairing fails contrast, it fails, full stop.

The default AI failure is to pick a nice-looking accent and call it a palette. A
palette is a *system of relationships*, chosen from a harmony, tuned by color
properties, and justified by psychology that fits the concept.

---

## 1. Start from the concept, not from a favorite color

Do not begin with "I'll use blue." Begin with the governing concept
(`craft/stylization.md`) and ask what *relationship* of colors expresses it:

- Is this surface **calm and singular** (one hue, many values → monochromatic /
  analogous) or **energetic and contrasting** (opposing hues → complementary /
  triadic)?
- Is it **grounded and neutral** with one point of life, or **saturated and loud**
  throughout?

The harmony type is a concept decision. Pick it first, then choose specific hues.

---

## 2. Harmony types (pick one relationship on purpose)

All are read off the color wheel (primary → secondary → tertiary relationships).

- **Monochromatic** — one hue, varied in value/saturation. Calm, cohesive,
  confident, easy to keep accessible. The safest route to "premium/minimal." Risk:
  can feel flat — rescue it with one small high-saturation moment.
- **Analogous** — 2–4 hues adjacent on the wheel (e.g. blue → teal → green).
  Natural, harmonious, low-tension. Great for organic/wellness/editorial moods.
  Pick one to dominate; the others support.
- **Complementary** — two opposite hues (blue/orange, red/green). Maximum contrast
  and energy; excellent for a CTA that must pop. Risk: vibration and fatigue if
  used 50/50 — use one as the field and the other *only* as the accent.
- **Split-complementary** — a base plus the two neighbors of its complement.
  Complementary's punch with less tension; more forgiving to balance.
- **Triadic** — three hues evenly spaced. Vibrant, playful, balanced. One primary,
  two accents — never three co-equal, or it turns to circus. Good for
  playful/creative brands.
- **Tetradic** — four hues (two complementary pairs). Rich but hard; needs one
  clear dominant and disciplined restraint on the rest. Use rarely and carefully.

**Reconciling with the one-accent lock:** the lock isn't "only one color exists."
Your neutrals carry the surface; the *accent* is the one saturated action/attention
color. A triadic scheme still resolves to one primary accent plus supporting hues
used sparingly (illustration, category tags, data series) — never as competing
CTAs. If two colors both shout "click me," you've broken the lock.

---

## 3. Color properties (the tuning knobs that decide the feeling)

Hue picks the *identity*; these three decide the *feeling* and do most of the
hierarchy work:

- **Value (lightness/darkness)** — the strongest tool for hierarchy and for
  contrast/accessibility. Most of a palette's "steps" are value steps of a few
  hues. Adding white (a *tint*) turns an aggressive color tranquil (bold yellow →
  calm pastel); adding black (a *shade*) adds weight and sophistication.
- **Saturation (intensity)** — the volume knob. High saturation advances and grabs;
  low saturation recedes and calms. **Reserve your highest saturation for the one
  thing that matters most** (the primary action, a live figure). A page where
  everything is saturated has no hierarchy — nothing can stand out when everything
  shouts.
- **Temperature (warm/cool)** — warm hues (red/orange/yellow) advance and energize;
  cool hues (blue/green/violet) recede and calm. Temperature sets the emotional
  baseline before hue-specific meaning even registers. Choose a temperature for the
  neutrals *intentionally* (warm grey vs. cool grey completely changes the mood) and
  hold it — the main skill's "warm or cool, chosen and held" rule.

Practical consequence: **hierarchy and mood are mostly value + saturation, not
hue.** You can build an entire expressive, accessible palette from *one* hue by
moving value and saturation, then add a single complementary accent for the one
moment that must pop.

---

## 4. Color psychology (justify the hue against the concept)

Color carries emotional and cultural payload; use it to reinforce the concept, and
make it defensible rather than decorative. Common Western associations (interpret,
don't just apply — see the lookup-vs-interpretation warning in
`craft/stylization.md`):

| Hue | Common associations | Typical use |
|---|---|---|
| **Blue** | Trust, calm, reliability, professionalism; dark blue = tranquil + sophisticated | Finance, health, B2B, security |
| **Green** | Growth, nature, health, "go/proceed"; also money | Wellness, sustainability, success states |
| **Red** | Urgency, passion, appetite, error/warning | Alerts, sales, food; use sparingly as accent |
| **Yellow** | Optimism, energy, attention, knowledge | Highlights, kids/education, warnings (amber) |
| **Orange** | Warmth, friendliness, stimulation, affordability | CTAs, playful/creative, energetic brands |
| **Purple** | Luxury, creativity, wisdom, the unconventional | Premium, beauty, fintech/crypto, creative tools |
| **Black / near-black** | Sophistication, authority, premium | Luxury, editorial, high-contrast minimal |
| **Warm neutrals** | Calm, human, editorial, approachable | Content-first, wellness, craft brands |
| **Cool neutrals / grey** | Clean, modern, technical, focused | Productivity, enterprise, product-forward |

Two rules on top of the table:

- **Meaning is contextual, not absolute.** Culture flips it (red = danger vs.
  fortune); so does saturation and value (a pastel red is not an alarm). The
  *interpretation* of the audience decides which reading applies.
- **Semantic states are reserved.** Keep a warm bright hue (usually red/amber) for
  warnings and errors — don't spend your one hot accent on it *and* on the brand,
  or an error won't read as an error. Green for success/proceed, red for
  destructive/error, amber for caution, blue/neutral for info.

---

## 5. Building the palette (a working method)

1. **Concept → harmony type** (§1–2). Decide mono/analogous/complementary/triadic.
2. **Choose the neutrals first.** 4–5 steps from background to primary text,
   off-black/off-white, warm or cool per the concept. The neutrals are 90% of the
   pixels; they set the mood more than the accent does.
3. **Choose one accent.** The single saturated color for primary action/attention.
   Its hue is justified by psychology (§4); its saturation is high *because* it's
   the one thing meant to pop (§3).
4. **Add semantic states** if the surface needs them, kept distinct from the
   accent.
5. **Light and dark:** if the surface supports both, maintain *hierarchy parity*
   (the same things stand out in both) and keep the accent recognizable across
   modes. Dark mode is not "invert" — re-tune value and saturation so contrast and
   mood survive.
6. **Audit against the floor:** every text/background pair, button, input,
   placeholder, focus ring, and disabled state at AA (4.5:1 body, 3:1 large/UI).
   Never rely on hue alone to carry meaning (color-blind users) — pair color with
   text, icon, or shape.

---

## 6. Common color slop to avoid

- **Accent-first, no system** — a pretty accent bolted onto default greys, no
  chosen harmony or temperature. The most common tell.
- **Everything saturated** — no value/saturation hierarchy, so nothing leads.
- **The AI-default palette** — auto purple/blue glow gradient as the reflex.
  Choose color from the concept instead (main skill §3).
- **Uncommitted neutrals** — greys with no chosen temperature, reading as "system
  default." Pick warm or cool and hold it.
- **Accent doubling as an error color** — brand red *and* alert red; the alert
  loses its signal.
- **Too many hues at equal weight** — more than ~2 primary + 2 secondary at similar
  value/saturation flattens perceived hierarchy (NN/g). Give one hue clear
  dominance.

---

## Handoff

The palette you build here fills the **Palette** slot of the style contract
(Step 1) and must express the concept from `craft/stylization.md`. How those colors
are *deployed* to lead the eye — what gets the saturated moment, what recedes — is
composition; see `craft/composition.md`.
