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

    self.perim = 0

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
    for neighbor in (cur.up, cur.down, cur.left, cur.right):
      if neighbor and neighbor.label == cur.label:
        if neighbor in remaining:
          remaining.remove(neighbor)
          frontier.add(neighbor)
          region.add(neighbor)
      else:
        cur.perim += 1
  regions.append(region)

cost = 0
for region in regions:
  cost += len(region) * sum(plant.perim for plant in region)

print(cost)
