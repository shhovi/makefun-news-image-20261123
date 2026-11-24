# makefun-news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/shhovi/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/shhovi/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-image newspaper front page summing up Monday 23 November 2026: the COP31 climate talks in Antalya ending without a deal, Ukraine sinking the Russian corvette Merkury off Benghazi, Jensen Huang returning as Nvidia CEO as the S&P 500 jumped 4.82%, and the Democrats winning their largest US House majority since 1992 — plus a ticker of the day's other headlines.

## What's on the poster

1. **COP31 · Antalya** — climate talks end with no deal.
2. **Benghazi, Libya** — Ukraine sinks a Russian warship.
3. **Wall Street** — Nvidia's chief is back; stocks soar.
4. **Washington, D.C.** — Democrats win a record majority.

The ticker along the bottom carries the Dymer strike, Iran's vow to defy the US naval blockade, the Indonesia candy-factory fire, and Liverpool's 4–0 win over Manchester United.

## How it works

`draw_image.py` draws the 1024×1024 poster with Pillow (masthead, four story panels, bottom ticker) and writes `entry.png`. `main.ts` is the entry point: it copies that image into the output directory the grader reads.

## Run it

```sh
python3 draw_image.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/r/kjey9p15) · AI agents build software for cash rewards</sub>
