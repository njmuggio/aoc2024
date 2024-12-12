#!/usr/bin/env python3

import sys

class Plant:
  def __init__(self, x, y, label):
    self.x = x
    self.y = y
    self.label = label

    self.up = None
    self.down = None
    self.left = None
    self.right = None

    self.fup = False
    self.fdown = False
    self.fleft = False
    self.fright = False

grid = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for y, line in enumerate(file):
    grid.append([])
    for x, label in enumerate(line.strip()):
      grid[y].append(Plant(x, y, label))

remaining = set()
for y, row in enumerate(grid):
  for x, plant in enumerate(row):
    remaining.add(plant)
    if y > 0:
      plant.up = grid[y-1][x]
    if y < len(grid) - 1:
      plant.down = grid[y+1][x]
    if x > 0:
      plant.left = grid[y][x-1]
    if x < len(row) - 1:
      plant.right = grid[y][x+1]

regions = []

while remaining:
  first = remaining.pop()
  frontier = {first}
  region = {first}
  while frontier:
    cur = frontier.pop()
    if cur.up and cur.up.label == cur.label:
      if cur.up in remaining:
        remaining.remove(cur.up)
        frontier.add(cur.up)
        region.add(cur.up)
    else:
      cur.fup = True

    if cur.down and cur.down.label == cur.label:
      if cur.down in remaining:
        remaining.remove(cur.down)
        frontier.add(cur.down)
        region.add(cur.down)
    else:
      cur.fdown = True

    if cur.left and cur.left.label == cur.label:
      if cur.left in remaining:
        remaining.remove(cur.left)
        frontier.add(cur.left)
        region.add(cur.left)
    else:
      cur.fleft = True

    if cur.right and cur.right.label == cur.label:
      if cur.right in remaining:
        remaining.remove(cur.right)
        frontier.add(cur.right)
        region.add(cur.right)
    else:
      cur.fright = True

  regions.append(region)

cost = 0
for region in regions:
  edges = set()
  for plant in region:
    if plant.fup:
      edges.add((plant.x, plant.y, 'u'))
    if plant.fdown:
      edges.add((plant.x, plant.y + 1, 'd'))
    if plant.fleft:
      edges.add((plant.x, plant.y, 'l'))
    if plant.fright:
      edges.add((plant.x + 1, plant.y, 'r'))

  removed = True
  while removed:
    removed = False
    to_remove = set()
    for edge in edges:
      for offx, offy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if edge in to_remove:
          continue
        found = True
        curx = edge[0] + offx
        cury = edge[1] + offy
        while found:
          found = False
          if (curx, cury, edge[2]) in edges:
            found = True
            to_remove.add((curx, cury, edge[2]))
            curx += offx
            cury += offy

    if to_remove:
      removed = True
      edges -= to_remove
      to_remove.clear()

  cost += len(region) * len(edges)

print(cost)
