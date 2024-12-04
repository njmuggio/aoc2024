#!/usr/bin/env python3

import sys

rows = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    rows.append(line.strip())

found = 0
offsets = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
word = "XMAS"
for y in range(len(rows)):
  for x in range(len(rows[y])):
    for offset in offsets:
      if y + offset[0] * 3 < 0 or y + offset[0] * 3 >= len(rows) or x + offset[1] * 3 < 0 or x + offset[1] * 3 >= len(rows[y]):
        continue
      if all(rows[y + offset[0] * idx][x + offset[1] * idx] == c for idx, c in enumerate(word)):
        found += 1

print(found)
