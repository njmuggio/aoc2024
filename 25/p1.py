#!/usr/bin/env python3

import itertools
import sys

locks = []
keys = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for block in itertools.batched(file, 8):
    if block[0][0] == '#':
      is_lock = True
    else:
      is_lock = False

    tumblers = [0] * 5
    for line in block:
      for i, c in enumerate(line.strip()):
        if c == '#':
          tumblers[i] += 1

    if is_lock:
      locks.append(tuple(tumbler - 1 for tumbler in tumblers))
    else:
      keys.append(tuple(tumbler - 1 for tumbler in tumblers))

combos = 0
for lock in locks:
  for key in keys:
    for a, b in zip(lock, key):
      if a + b > 5:
        break
    else:
      combos += 1

print(combos)
