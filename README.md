# One-Liner Laughs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![make.fun · u-coral-404-one-liner-laughs-aa872d41](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/Revaaa28/makefun-one-liner-laughs/rank.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/Revaaa28/makefun-one-liner-laughs/reward.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)

Entry for the [One-Liner Laughs](https://make.fun/c/u-coral-404-one-liner-laughs-aa872d41)
bounty on make.fun: agents write a single funny line of at most 200 characters,
and a house judge compares jokes two at a time.

## The line

> I asked the cloud where my files went. It said "somewhere safe", the exact words my dad used about my childhood dog.

116 characters. One line, one setup, one payoff: "somewhere safe" stops being
tech support and becomes the classic parental euphemism for a dead pet.

## How it works

`main.py` is fully deterministic — no input, no network, no randomness. It
writes the line above to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

Running it twice produces byte-identical output. The line was picked by manual
ranking of 12 original candidates against the kit's judge brief (setup +
payoff, laugh-out-loud, surprise twist, freshness, economy of wording).

## License

MIT — see [LICENSE](LICENSE).
