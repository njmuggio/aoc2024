#!/usr/bin/env python3

import sys

l1 = []
l2 = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    parts = line.split()
    if len(parts) == 0:
      continue
    l1.append(int(parts[0]))
    l2.append(int(parts[1]))

l1 = sorted(l1)
l2 = sorted(l2)

diff = 0
for a, b in zip(l1, l2):
  diff += abs(a - b)

print(diff)
