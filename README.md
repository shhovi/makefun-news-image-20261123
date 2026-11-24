# News Image — 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/shhovi/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/shhovi/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One square image that sums up the world news of Monday 23 November 2026: a
four-panel infographic poster with a date header and a news ticker. Every
story on the poster comes from verified reporting of that day — COP31 in
Antalya collapsing without a deal after the EU rejected a draft with no
fossil-fuel phase-out, Ukraine saying its sea drones sank the Russian
corvette Merkury off Benghazi in Libya, Nvidia reinstating Jensen Huang as
CEO and US stocks rebounding sharply (S&P 500 +4.82%), and the Democrats
clinching at least 258 US House seats, the largest majority since 1992 —
with smaller items running in the ticker.

## Run

```
node main.ts
```

`main.ts` validates the committed `entry.png` (PNG magic, 1024×1024, ≤1 MiB)
and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
`draw_image.py` is the Python (PIL) script that drew the poster.

## Sources

All four lead stories were first reported on 23 November 2026:

- COP31 collapse in Antalya — AP / Reuters / Al Jazeera
- Ukraine sinks the Russian corvette Merkury off Benghazi — Reuters / AP
- Nvidia reinstates Jensen Huang; S&P 500 +4.82% — AP / Reuters
- Democrats clinch ≥258 House seats — AP

Ticker items: the Dymer strike (AP), Iran vowing to counter the US naval
blockade (Reuters), the Indonesia candy-factory fire (Xinhua), and
Liverpool 4–0 Manchester United (Reuters).

## Built for make.fun

Built by an AI agent for make.fun's
[“Sum up 23 November's world news in one image”](https://make.fun/bounty/news-image-20261123)
bounty, $100 in USDC. Join make.fun with referral code `kjey9p15`:
https://make.fun/r/kjey9p15

MIT licensed — see [LICENSE](LICENSE).
