#!/usr/bin/env python3

import sys

def test(ax, ay, bx, by, px, py, ca, cb):
  n = (by * px - bx * py) / (ax * by - ay * bx)
  m = (ay * px - ax * py) / (ay * bx - ax * by)
  if int(n) == n and int(m) == m:
    return int(n * ca + m * cb)
  return None

skip = True
total = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  lines = file.readlines()
  while lines:
    linea, lineb, linep, lines = lines[0], lines[1], lines[2], lines[4:]
    linea = linea.split()
    ax = int(linea[2][2:-1])
    ay = int(linea[3][2:])
    lineb = lineb.split()
    bx = int(lineb[2][2:-1])
    by = int(lineb[3][2:])
    linep = linep.split()
    px = int(linep[1][2:-1]) + 10_000_000_000_000
    py = int(linep[2][2:]) + 10_000_000_000_000

    cost = test(ax, ay, bx, by, px, py, 3, 1)
    if cost is not None:
      total += cost

print(total)
