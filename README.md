[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/giandisruw/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/giandisruw/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)

# Two-Sentence Horror

Entry for the make.fun bounty [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253) — the scariest horror story you can tell in exactly two sentences, up to 400 characters, judged blind in pairwise rounds by a horror editor who is hard to frighten.

## The story

**Every night my daughter tucks her doll in beside her and whispers goodnight to the man in the corner. Tonight the doll was already tucked in, and the whispering was coming from her bedroom — in her voice — while she stood beside me in the hall.**

Character count: **244** (limit: 400). Sentences: **2**.

## How it works

`main.py` (Python 3, standard library only) writes exactly that story to `/output/entry.txt` — no trailing newline, nothing else. Before writing, it validates the story: 1–400 characters, exactly two sentences, no leading or trailing whitespace, no control characters. No network, no randomness, no API key, no input, so the output is byte-identical on every run.

```bash
python3 main.py
```

To verify the entry yourself — validation, two independent writes, a byte comparison, and the character and sentence counts — run the built-in self-test:

```bash
python3 main.py --self-test
```

It prints the story, its character and sentence counts, a PASS/FAIL verdict for each check, and exits 0 only if every check passes. It writes only to a fresh temporary directory and leaves `/output/entry.txt` untouched.

## Why it is frightening

The first sentence sets a nightly ritual the narrator has accepted as harmless: a child whispering goodnight to "the man in the corner". The second sentence turns it — the ritual happens without the child. The doll is already tucked in, and the whispering is still going, in the daughter's own voice, while the real daughter stands beside the narrator in the hall. Whatever is in the room has learned to sound like her, and it has been practising every night. The horror is implied, never explained: no gore, no monster described, only the reader filling in what has been whispering back all this time — and what it wants next.

## Choosing the story

Three candidates were actually considered; the winner won on the turn, the implication, and the originality.

1. **"Every night my daughter tucks her doll in beside her and whispers goodnight to the man in the corner. Tonight the doll was already tucked in, and the whispering was coming from her bedroom — in her voice — while she stood beside me in the hall."** — 244 chars. **Winner.** The second sentence reframes the first: the nightly ritual was never only the daughter's habit, and something in the room can now sound like her. Concrete, implied, and the dread grows on a second read.
2. **"I finally changed the locks after my ex kept letting himself in, and I slept soundly for the first time in months. This morning the deadbolt was locked from the inside, and there was a second toothbrush in the holder, still wet."** — 232 chars. A good turn — the threat is inside, not outside — but the "ex who won't leave" setup is a familiar one, and the scare is a situation rather than a revelation about the first sentence.
3. **"For three years I have waved at the old man who watches my morning run from his porch, and today he finally waved back. He waved with my hand — the one I lost in the accident last winter."** — 182 chars. A striking image, but it leans on body horror and leaves the reader puzzling over the mechanics instead of feeling the dread; restraint matters more than shock.

The first draft of the winner was flatter — "Every night my daughter tucks her doll in beside her and whispers goodnight to the man in the corner. Tonight the doll was already tucked in when I checked on her, and I heard whispering from her bedroom — in her voice — while she stood beside me in the hall." (259 chars) — and the revision cut the dead "when I checked on her" clause and tied the sound back to the nightly ritual with "the whispering was coming from", so the turn lands on the reader instead of being narrated to them. See the revision note in `main.py`.

Referral code: 0txwmf1m

## License

MIT — see [LICENSE](LICENSE).
