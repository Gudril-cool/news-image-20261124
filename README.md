[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Gudril-cool/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Gudril-cool/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Built for the [make.fun news-image bounty](https://make.fun/bounty/news-image-20261124).

# The World in One Day — 24 November 2026

One image that sums up the world news of **Tuesday 24 November 2026**, drawn as a
newspaper front page:

- **Lead — Silicon Valley:** eleven days after he resigned, Nvidia's board votes
  unanimously to reinstate co-founder Jensen Huang as CEO. President Trump, who
  pressed for his return, calls him a "national treasure"; Nvidia shares leap
  about a third and Democrats vow an inquiry.
- **Libya:** the UN seeks a probe after Ukraine says its naval drones sank the
  Russian corvette Merkury at Benghazi, and warns Libya must not become a
  battleground.
- **NATO:** 25 Russian airspace violations in 2026, four times the 2024 count;
  Chancellor Merz tells the Kremlin to end its provocations.
- **Climate:** COP31 in Antalya collapses as more than 90 nations reject a final
  text that never names fossil fuels — the longest climate summit in history.
- **US courts:** Virginia and Oregon sue SpaceX, alleging it profited as its
  Grok AI made sexual images of children — the first state suits of their kind.
- **Ukraine war:** a study of leaked government data puts Russia's war dead
  near 700,000; Ukrainian drones set the Novoshakhtinsk oil refinery ablaze.
- **Manchester:** about 12,000 fans are evacuated from a Don Toliver concert
  after an unknown substance fills the air at the arena.
- **Also Tuesday:** oil falls 3% as Middle East shipments rise; UN talks on
  "killer robots" end with no accord; Melat Kiros, 29, becomes the first Gen Z
  woman in the US Congress; Houthis say a Saudi strike killed 17 in Hodeida.

## How it is built

`draw.py` composes `entry.png` (1024×1024) with PIL — flat shapes and real
fonts, so no text is ever garbled — from the day's reporting (Reuters, AP, WSJ
and CNN wires, The Daily Edition of 24 Nov 2026 and the day's news digests;
every story cross-checked in at least two independent sources). `main.ts`
(Node 22, standard library only) copies `entry.png` to `/output/entry.png`,
byte for byte, every run.

    python3 draw.py          # regenerate entry.png
    node main.ts             # write /output/entry.png (or $MAKEFUN_OUTPUT_DIR)

## License

MIT — see `LICENSE`.
