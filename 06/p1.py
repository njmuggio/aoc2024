#!/usr/bin/env python3

import sys

grid = []
x = 0
y = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    if "^" in line:
      y = len(grid)
      x = line.find("^")
      line = line.replace("^", "X")
    grid.append([c for c in line.strip()])

offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_dir = 0


while True:
  if y + offsets[cur_dir][0] < 0 or y + offsets[cur_dir][0] >= len(grid) or x + offsets[cur_dir][1] < 0 or x + offsets[cur_dir][1] >= len(grid[0]):
    break
  if grid[y + offsets[cur_dir][0]][x + offsets[cur_dir][1]] == '#':
    cur_dir = (cur_dir + 1) % len(offsets)
  else:
    y += offsets[cur_dir][0]
    x += offsets[cur_dir][1]
    grid[y][x] = 'X'

tot = 0

for row in grid:
  tot += row.count('X')
print(tot)
