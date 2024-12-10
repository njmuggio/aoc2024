#!/usr/bin/env python3

import sys

class Cell:
  def __init__(self, x, y, height):
    self.x = x
    self.y = y
    self.height = height

    self.up = None
    self.down = None
    self.left = None
    self.right = None

    self.trails = 0
    self.accessible = set()


grid = []
cells = {}
for height in range(10):
  cells[height] = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for y, line in enumerate(file):
    grid.append([])
    for x, c in enumerate(line.strip()):
      height = int(c) if c != '.' else -1
      cell = Cell(x, y, height)
      grid[y].append(cell)
      if height in cells:
        cells[height].append(cell)

for y, row in enumerate(grid):
  for x, cell in enumerate(row):
    if y > 0:
      cell.up = grid[y-1][x]
    if y < len(grid) - 1:
      cell.down = grid[y+1][x]
    if x > 0:
      cell.left = grid[y][x-1]
    if x < len(row) - 1:
      cell.right = grid[y][x+1]

for cell in cells[9]:
  cell.trails = 1
  cell.accessible.add(cell)

for height in range(8, -1, -1):
  for cell in cells[height]:
    if cell.up and cell.up.height == cell.height + 1:
      cell.trails += cell.up.trails
      cell.accessible.update(cell.up.accessible)
    if cell.left and cell.left.height == cell.height + 1:
      cell.trails += cell.left.trails
      cell.accessible.update(cell.left.accessible)
    if cell.right and cell.right.height == cell.height + 1:
      cell.trails += cell.right.trails
      cell.accessible.update(cell.right.accessible)
    if cell.down and cell.down.height == cell.height + 1:
      cell.trails += cell.down.trails
      cell.accessible.update(cell.down.accessible)

total = 0
accessible = 0
for cell in cells[0]:
  total += cell.trails
  accessible += len(cell.accessible)

print(accessible)
