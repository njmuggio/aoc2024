#!/usr/bin/env python3

import sys

def hash(seed, iters):
  for _ in range(iters):
    seed = (seed ^ (seed << 6)) & 0xFFFFFF
    seed = ((seed >> 5) ^ seed) & 0xFFFFFF
    seed = ((seed << 11) ^ seed) & 0xFFFFFF
  return seed

total = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    total += hash(int(line.strip()), 2000)

print(total)
