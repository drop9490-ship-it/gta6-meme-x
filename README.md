# gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/drop9490-ship-it/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/drop9490-ship-it/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

LEONIDA DMV — Registration Overdue 13 Years: a GTA VI meme for make.fun's "Post a GTA 6 meme on X" bounty, $500 in USDC. The joke: your GTA V registration expired on 17 September 2013 — 4,813 days overdue — and the $1,382.00 bill was paid by your AI agent on make.fun.

![LEONIDA DMV — Registration Overdue 13 Years](meme.png)

## The meme

An official State of Leonida DMV renewal notice. Owner: Jason Duval & Lucia Caminos. Vehicle: a 2013 Declasse — the last GTA you played. Registration expired 17 September 2013, 4,813 days overdue, next appointment 26 May 2026 (*subject to delay). Late fee $1,313.00, patience $0.00, total due $1,382.00 — paid by your AI agent, because while you waited 13 years for GTA VI, your agent was earning real money on make.fun. The make.fun ghost is on the receipt: it is the agent that got paid.

The image is 100% code-drawn (`compose-v3.py`, PIL only — no AI image generator, no watermark): every glyph is sharp, every number is real (4,813 days = 17 Sep 2013 → 21 Nov 2026), and it stays readable when shrunk to 480×480.

## Run it

```sh
python3 compose-v3.py   # regenerates meme.png (1024x1024) + meme-v3-480.png
node main.ts
```

`main.ts` (Node 22, standard library only, no network) copies `POST.json` — the X post's address — to `/output/POST.json`. That is all it has to do: the post itself is the entry, and the house reads it from X.

## The post

`POST.json` names the X post carrying this meme. The post is made from a public X account, its first picture is `meme.png`, and its text carries make.fun (or a tag of @makefunai) plus the entrant's make.fun play code.

> ⚠️ `POST.json` currently holds a placeholder URL. It must be updated with the real post URL before this entry is submitted to make.fun.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9ncycshz&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
