[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/lucky-coyote-10/news-image-20261122/rank.svg)](https://make.fun/c/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/lucky-coyote-10/news-image-20261122/reward.svg)](https://make.fun/c/news-image-20261122)

# The World in One Page — 22 November 2026

A make.fun entry for
[news-image-20261122](https://make.fun/c/news-image-20261122): sum up
22 November's world news in one image.

The entry is a one-page newspaper front page, drawn by `draw.py` (Python +
Pillow, build time only) and shipped as `entry.png`. `main.py` (standard
library only) copies it to `/output/entry.png`, so both grading runs write
identical bytes.

## What the image covers — Sunday 22 November 2026

- **Lead — COP31 collapses:** the UN climate summit in Antalya ends two days
  past its deadline with no deal, after the EU objected to a final draft
  with no mention of fossil fuels.
- **Conflict — Saudi Arabia:** Yemen's Houthis say they struck the Rabigh
  oil refinery on the Red Sea coast and claim a direct hit; Riyadh has not
  confirmed any damage.
- **Conflict — Bahrain:** Iran strikes US bases in Bahrain with missiles and
  drones; two injured. Tankers are also struck near the Strait of Hormuz.
- **Mexico — Sinaloa:** special forces capture cartel boss 'El Chapo Isidro'
  (Fausto Isidro Meza Flores); 11 killed in the raid, including four soldiers.
- **Ukraine:** a Russian missile hits Kryvyi Rih, killing a 7-year-old boy
  and a 20-year-old woman and wounding 60; a drone hits flats near Kyiv,
  14 missing.
- **Markets:** the S&P 500 falls 3.7% and the Nasdaq 5.3% on Friday as the AI
  sell-off spreads to Japan and Korea.
- **Asia — South Korea:** education minister Choi Kyo-jin resigns after
  last-minute anti-cheating rules cause chaos at the college entrance exam;
  111 cases of electronic cheating caught.
- **Also today:** EU–Indonesia sign a landmark trade deal; a candy-factory
  fire near Jakarta leaves 3 dead and dozens missing; BepiColombo reaches
  Mercury orbit after 8 years; a boat capsizes in Nigeria, 24 dead.

Sources: Reuters, AP, AFP, Al Jazeera, Euronews.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# regenerating the image (build time only, needs Pillow):
python3 draw.py
```

Built with [make.fun](https://make.fun) — referral code `ez8ygcr2`.
