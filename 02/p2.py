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
    else:
      for excl_idx in range(len(levels)):
        dampened = levels.copy()
        del dampened[excl_idx]
        dampened_diffs = []
        for i in range(1, len(dampened)):
          dampened_diffs.append(dampened[i] - dampened[i - 1])
        if all(-3 <= d <= -1 for d in dampened_diffs) or all(1 <= d <= 3 for d in dampened_diffs):
          good += 1
          break

print(good)
