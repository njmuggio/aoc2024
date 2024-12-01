#!/usr/bin/env python3

import sys

l1 = []
l2 = {}
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    parts = line.split()
    if len(parts) == 0:
      continue
    i1 = int(parts[0])
    i2 = int(parts[1])
    l1.append(i1)
    if i2 in l2:
      l2[i2] += 1
    else:
      l2[i2] = 1

total = 0
for n in l1:
  total += n * l2[n] if n in l2 else 0

print(total)
