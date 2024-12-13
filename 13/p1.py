#!/usr/bin/env python3

import sys

def test(ax, ay, bx, by, px, py, ca, cb):
  m = None
  for na in range(101):
    curx = ax * na
    cury = ay * na

    if curx > px or cury > py:
      return m

    remainx = px - curx
    remainy = py - cury

    if remainx % bx == 0 and remainx / bx == remainy / by:
      nb = remainx // bx
      cost = na * ca + nb * cb
      if m is None or cost < m:
        m = cost

  return m

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
    px = int(linep[1][2:-1])
    py = int(linep[2][2:])

    cost = test(ax, ay, bx, by, px, py, 3, 1)
    if cost is not None:
      total += cost

print(total)
