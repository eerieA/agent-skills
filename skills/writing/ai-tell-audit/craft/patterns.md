# AI tell catalog

The patterns that mark prose as machine-generated, grouped by kind. Each entry has
a tier (see `SKILL.md`) and a before → after. **High** flags standalone; **Medium**
flags only in a cluster; **Voice** flags only for expressive registers.

Read `false-positives.md` before writing any finding - several of these patterns
occur in clean human writing and are only tells when they cluster.

---

## A. Wording

### A1. Significance / legacy inflation - High
Puffing up importance by asserting that something represents a broader trend, marks
an era, or leaves a legacy.

Watch: *stands/serves as, is a testament/reminder, plays a vital/crucial/pivotal/key
role, underscores/highlights its importance, reflects broader, marking a shift, key
turning point, indelible mark, deeply rooted, enduring/lasting legacy.*

- Before: *Established in 1989, it marked a pivotal moment in the evolution of
  regional statistics.*
- After: *Established in 1989 to collect and publish regional statistics.*

### A2. Promotional / advertisement tone - High
Neutral facts dressed up as a brochure. Worst on place, culture, and product topics.

Watch: *boasts, vibrant, rich (figurative), breathtaking, nestled, in the heart of,
must-visit, stunning, renowned, groundbreaking, revolutionary, transformative,
cutting-edge, state-of-the-art, unparalleled, seamless.*

The puffery phrase list below (spanning A1 + A2) is refreshed from Wikipedia by
scripts/sync-wikipedia.py; hand-written guidance around it stays untouched.

> AUTO-GENERATED PUFFERY - do not hand-edit below; refreshed by scripts/sync-wikipedia.py
<!-- SYNC:PUFFERY:START -->
boasts, breathtaking, commitment to, contributing to the, cutting-edge,
deeply rooted, enduring legacy, evolving landscape, exemplifies, focal point,
groundbreaking, in the heart of, indelible mark, is a testament,
key turning point, must-visit, nestled, plays a vital role, profound,
reflects broader, renowned, rich tapestry, seamless, setting the stage for,
stands as, state-of-the-art, stunning, transformative,
underscores its importance, unparalleled
<!-- SYNC:PUFFERY:END -->

- Before: *Nestled in the breathtaking Gonder region, the town boasts a rich
  cultural heritage and stunning natural beauty.*
- After: *A town in the Gonder region, known for its weekly market and 18th-century
  church.*

### A3. Overused AI vocabulary - Medium
Words that spike in post-2023 text and tend to co-occur. One is nothing; three in a
paragraph is a cluster.

Watch: *delve, tapestry, testament, leverage (as filler), robust, holistic,
comprehensive (when "complete" works), pivotal, paramount, intricate/interplay,
underscore, showcase, garner, foster, align with, crucial, vital, ever-evolving,
in today's world.*

> AUTO-GENERATED VOCAB - do not hand-edit below; refreshed by scripts/sync-wikipedia.py
<!-- SYNC:VOCAB:START -->
actually, additionally, align, boasts, bolstered, crucial, delve, emphasize,
emphasizing, enduring, enhance, foster, fostering, garner, highlight,
highlighting, interplay, intricate, key, landscape, pivotal, showcase,
showcasing, tapestry, testament, underscore, valuable, vibrant
<!-- SYNC:VOCAB:END -->

- Before: *Additionally, an enduring testament to Italian influence is the vibrant
  culinary landscape, showcasing how dishes integrated into the diet.*
- After: *Pasta dishes, introduced during Italian colonization, remain common,
  especially in the south.*

### A4. Vague attribution / weasel words - Medium
Opinions pinned on nobody in particular.

Watch: *experts argue, observers have cited, industry reports, some critics say,
it is believed, several sources* (when few are named).

- Before: *Experts believe it plays a crucial role in the regional ecosystem.*
- After: *It supports several endemic fish species, per a 2019 Academy survey.*

### A5. Filler and hedging - Medium
Phrases that add length, not meaning; or over-qualified claims.

- *in order to* → *to*; *due to the fact that* → *because*; *at this point in time*
  → *now*; *has the ability to* → *can*; *it is important to note that* → (drop).
- Before: *It could potentially possibly be argued that the policy might have some
  effect.*
- After: *The policy may affect outcomes.*

### A6. Authority tropes - Medium
Pretending to cut through noise to a deeper truth, then restating an ordinary point.

Watch (sentence-start): *at its core, in reality, fundamentally, what really matters,
the real question is, the heart of the matter, the deeper issue.*

- Before: *At its core, what really matters is organizational readiness.*
- After: *That mostly depends on whether the organization will change its habits.*

### A7. Aphorism formulas - Medium
Turning a plain claim into a portable-sounding maxim.

Watch: *X is the Y of Z, X becomes a trap, not a tool but a mirror, the language of,
the currency of, the architecture of.*

- Before: *Symmetry is the language of trust.*
- After: *Symmetric layouts often feel more predictable to users.*

---

## B. Structure

### B1. Rule of three - Medium
Forcing ideas into triples to sound complete. Two often suffice; use the number that
fits.

- Before: *keynote sessions, panel discussions, and networking opportunities...
  innovation, inspiration, and industry insights.*
- After: *talks and panels, plus time for informal networking.*

### B2. Negative parallelism / binary contrast - High
The telegraphed reversal. Overused enough to be a strong tell on its own.

Watch: *not X but Y; it's not just X, it's Y; isn't X, it's Y; the answer isn't X,
it's Y; stops being X and starts being Y; not X. But Y.*

- Before: *It's not merely a song, it's a statement.*
- After: *The song works as a political statement.*

### B3. Negative listing - Medium
A striptease of what something is *not* before the reveal.

- Before: *Not a warning. Not a suggestion. A command.*
- After: *A command.*

### B4. "Despite challenges" / future-outlook sections - Medium
The formulaic "Challenges and Future Prospects" shape.

- Before: *Despite these challenges, with its strategic location, the town continues
  to thrive.*
- After: *A 2022 stormwater project began addressing the recurring floods.*

### B5. Superficial -ing analyses - High
Present-participle tails bolted on to fake depth.

Watch: *highlighting..., ensuring..., reflecting..., symbolizing..., contributing
to..., showcasing...* appended to an otherwise complete sentence.

- Before: *The palette resonates with the region, symbolizing the coast, reflecting
  the community's deep connection to the land.*
- After: *The architect chose the colors to reference the local coast.*

### B6. Fragmented headers - Medium
A heading followed by a one-line paragraph that just restates the heading.

- Before: `## Performance` / *Speed matters.* / *When users hit a slow page...*
- After: `## Performance` / *When users hit a slow page...*

### B7. Diff-anchored writing - Medium
Docs/comments that narrate a change instead of describing the thing as it is (unless
the doc is inherently version-scoped: changelogs, migration guides).

- Before: *This function was added to replace the previous O(n²) approach.*
- After: *This function uses a hash map for O(1) lookups.*

### B8. Rhetorical setups / signposting - Medium
Announcing the point instead of making it.

Watch: *let's dive in, let's break this down, here's what you need to know, what if
[reframe]?, here's what I mean, think about it.*

- Before: *Let's dive into how caching works. Here's what you need to know.*
- After: *Next.js caches at several layers: request memoization, data cache, router
  cache.*

---

## C. Voice & tone

These are Voice-tier: flag only for expressive registers (essay, blog, personal,
marketing), never for reference/technical text, where neutral plainness is correct.

### C1. Soulless-but-clean prose - Voice
Technically tell-free, but every sentence is the same length, no opinion, no
first person, no uncertainty. Reads like a press release.

- Before: *The experiment produced interesting results. Some were impressed, others
  skeptical. The implications remain unclear.*
- After: *I don't know how to feel about this. Half the people I trust are thrilled;
  the other half think it's a parlor trick. I keep landing somewhere in between.*

### C2. Manufactured punchlines / staccato drama - Medium
Every sentence lands like a closer; short fragments stacked to fake momentum. One
short sentence for emphasis is fine; a run of them is engineered.

- Before: *Then it arrived. No preference for symmetry. No aesthetic prior. The old
  rules were gone.*
- After: *It changed the search because it didn't favor symmetry, which made some old
  assumptions less useful.*

### C3. Sycophantic / servile tone - High
People-pleasing filler, usually chatbot residue pasted into content.

Watch: *Great question! Certainly! You're absolutely right! I hope this helps! Let me
know if... Would you like me to...*

This also covers chatbot correspondence artifacts and prompt-refusal residue pasted
into content (*as an AI language model, I cannot..., I hope this email finds you
well*). The phrase list below is refreshed from Wikipedia by
scripts/sync-wikipedia.py.

> AUTO-GENERATED COMMS - do not hand-edit below; refreshed by scripts/sync-wikipedia.py
<!-- SYNC:COMMS:START -->
as a large language model, as an ai language model, certainly,
great question, here is a, i cannot provide,
i hope this email finds you well, i hope this helps, is there anything else,
let me know, let me know if, of course, would you like me to,
you're absolutely right
<!-- SYNC:COMMS:END -->

- Before: *Great question! You're absolutely right that this is complex.*
- After: (drop; state the point.)

### C4. Conversational fake-candor openers - Medium
A theatrical pause-and-reveal before an ordinary claim.

Watch (as standalone hooks): *Honestly? Look, Here's the thing, The thing is, Let's
be honest, Real talk.*

- Before: *Is it worth it? Honestly? It depends how often you'll use it.*
- After: *Whether it's worth it depends on how often you'll use it.*

### C5. False agency - Medium
Inanimate things given human verbs to avoid naming the actor.

- Before: *The complaint becomes a fix. The decision emerges.*
- After: *The team fixed it that week. She decided to ship it.*

### C6. Copula avoidance - Medium
Elaborate constructions dodging a plain *is/are*.

Watch: *serves as, stands as, represents, boasts, features, offers* where *is/has*
would do.

- Before: *Gallery 825 serves as the exhibition space and boasts 3,000 square feet.*
- After: *Gallery 825 is the exhibition space; it has 3,000 square feet.*

### C7. Generic positive conclusion - Medium
Vague upbeat endings that commit to nothing.

- Before: *The future looks bright. Exciting times lie ahead on the journey to
  excellence.*
- After: *The company plans to open two more locations next year.*

---

## D. Formatting & typography

### D1. Em / en dashes - High
One of the most reliable mechanical tells when paired with sales-y rhythm. Prefer a
period, comma, colon, or parentheses. Catch spaced ` - ` and double `--` too.

- Before: *The policy - announced without warning - affects thousands.*
- After: *The policy, announced without warning, affects thousands.*

### D2. Mechanical boldface - Medium
Bolding phrases reflexively, or inline-header lists (`**Term:** sentence`).

- Before: *It blends **OKRs**, **KPIs**, and the **Balanced Scorecard**.*
- After: *It blends OKRs, KPIs, and the Balanced Scorecard.*

### D3. Title Case In Headings - Medium
Capitalizing every main word. Prefer sentence case.

- Before: `## Strategic Negotiations And Global Partnerships`
- After: `## Strategic negotiations and global partnerships`

### D4. Emoji decoration - Medium
🚀 / ✅ / 💡 studding headings and bullets.

### D5. Curly quotes - Low
`"..."` for `"..."`. Weak on its own (editors auto-curl); a tell only when stacked
with others.

### D6. Elegant variation - Medium
Cycling synonyms to dodge repetition (*the protagonist... the main character... the
central figure... the hero*). Pick one term and reuse it.

### D7. False ranges - Medium
*from X to Y* where X and Y aren't on a real scale.

- Before: *from the singularity of the Big Bang to the enigmatic dance of dark
  matter.*
- After: *the Big Bang, star formation, and dark matter.*

### D8. Hyphenated-pair overuse - Low
*data-driven, cross-functional, high-quality, real-time* hyphenated uniformly, even
in predicate position. Keep the hyphen when attributive (*a high-quality report*),
drop it after the noun (*the report is high quality*).
