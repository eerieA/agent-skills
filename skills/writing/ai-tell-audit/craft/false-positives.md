# False positives - what is NOT a tell

The over-correction guard. Consult this **before** writing any finding. The failure
mode of this skill is gutting legitimate human prose because it pattern-matched a
coincidence. When unsure, do not flag.

## The cluster rule

A clean human writer hits many patterns in `patterns.md` without any AI involvement.
No single Medium/Low tell is evidence. Flag when tells **cluster** - several near
each other, or one pattern repeated - not when one appears alone.

A single em dash means nothing. Em dash **+** rule-of-three **+** "vibrant tapestry"
**+** a "Conclusion" section is a confession.

## Not reliable indicators on their own

- **Polished grammar and consistent style.** Many writers are professionals or have
  been edited. Polish is not AI.
- **Mixed casual/formal register.** Often signals a technical person, a young writer,
  or neurodivergent prose habits - not a chatbot.
- **"Bland" or "robotic" prose.** AI has *specific* tells. Generic dryness without
  them is just dry writing.
- **Formal/academic vocabulary.** AI overuses *specific* fancy words, not all of
  them. Don't flatten *ostensibly* or *constituent* for sounding brainy.
- **One transition word.** *Additionally / moreover / however* are tells only when
  piled up. One *however* is not.
- **Curly quotes alone.** macOS, Word, Google Docs, most CMSes auto-curl by default.
- **Em dashes alone.** Many editors and journalists use them heavily. Evidence only
  when paired with formulaic, sales-y rhythm.
- **One short emphatic sentence.** Humans use clipped sentences to land a point. Flag
  staccato drama only when several fragments run together.
- **"Honestly" / "look" mid-sentence.** Ordinary in casual writing. The tell is the
  standalone theatrical opener, not the word.
- **Unsourced claims.** Most of the web is unsourced. Absence of citations proves
  nothing.
- **Clean, complex formatting.** Templates and visual editors produce tidy output
  with no AI.

## Never touch (secondhand text)

Do not rewrite a watched phrase when it appears inside:
- Quotations, titles, proper names, or examples where the phrase is being *discussed*
  rather than *used*.
- Code, URLs, paths, commands, frontmatter (see the preserve-exactly list in
  `SKILL.md`).

## Register overrides voice findings

The Voice-tier tells (C-group) are **correct writing** for reference/technical/legal
text. Neutral, plain, opinion-free prose *is* the human voice there. Only flag
soullessness, missing first person, or absent opinion when the register is expressive
(essay, blog, personal, marketing). Injecting personality into an API doc is itself a
defect.

## Signs of a real human writing (lean toward leaving it alone)

- **Specific, hard-to-fabricate detail** - a real address, an odd quote, "the lawyer
  upstairs from my dentist". LLMs round specifics off; humans hoard them.
- **Mixed feelings, unresolved tension** - "mostly good, but it bothers me and I
  can't say why." LLMs default to clean takes.
- **Dated, era-bound references** - slang, memes, in-jokes tied to a year and
  subculture. Models lag.
- **Variety in sentence length** - real writing alternates short and long; AI trends
  to an even mid-length cadence.
- **Genuine asides and self-corrections** - "(I keep wanting to say 'almost' here,
  but it really was certain.)"
- **A choice the writer could defend.** If they can say *why* they cut a word or
  used one, that's a strong human signal.

When these are present, the prose is doing something a model rarely does. Preserve
it, even if it also trips a pattern.
