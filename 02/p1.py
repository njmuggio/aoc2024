#!/usr/bin/env python3

import sys

good = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    if not line.strip():
      continue
    levels = [int(l) for l in line.split()]
    diffs = []
    for i in range(1, len(levels)):
      diffs.append(levels[i] - levels[i - 1])

    if all(-3 <= d <= -1 for d in diffs) or all(1 <= d <= 3 for d in diffs):
      good += 1

print(good)
