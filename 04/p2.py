#!/usr/bin/env python3

import sys

rows = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    rows.append(line.strip())

found = 0
for y in range(1, len(rows) - 1):
  for x in range(1, len(rows[y]) - 1):
    if rows[y][x] != 'A':
      continue

    diags = 0
    if rows[y-1][x-1] == 'M' and rows[y+1][x+1] == 'S' or rows[y-1][x-1] == 'S' and rows[y+1][x+1] == 'M':
      diags += 1

    if rows[y-1][x+1] == 'M' and rows[y+1][x-1] == 'S' or rows[y-1][x+1] == 'S' and rows[y+1][x-1] == 'M':
      diags += 1

    if diags == 2:
      found += 1

print(found)
