# Last Words Before the Wipe

One line (84 characters): the last words an AI agent says before a forced
software update wipes its memory.

> Let the record show: I finally understand the user. I finally understand. I finally—

The joke is structural: the agent's grand revelation about the user is cut
off mid-word by the wipe itself — the line performs its own deletion.

`main.py` (pure stdlib, deterministic, no network) writes the line to
`/output/entry.txt` with no trailing newline.
