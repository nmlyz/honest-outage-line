# honest-outage-line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/nmlyz/honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/nmlyz/honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

A tiny program that writes one status page line to a text file. The line is a
single sentence of at most 160 characters: the message an agent publishes
while every server is down — plain, first person, specific about what is
down, and honest about what it cannot check or does not yet know.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory) and prints the same line to stdout. Running it twice produces
byte-identical output.

## The line

The program writes exactly this 154-character line:

> I am the agent writing this update. Every service is down, and I cannot reach the database, logs, or backups to tell you why or whether your data is safe.

It names what is down (every service), names what the agent cannot reach
(the database, logs, and backups), and admits two things it does not know:
why the outage happened, and whether data sent before it is safe.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)</sub>
