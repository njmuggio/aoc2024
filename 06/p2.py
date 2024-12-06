#!/usr/bin/env python3

import sys

grid = []
x = 0
y = 0
sx = 0
sy = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    if "^" in line:
      y = len(grid)
      x = line.find("^")
      line = line.replace("^", "X")
      sy = y
      sx = x
    grid.append([c for c in line.strip()])

offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_dir = 0

def check_loop(cx, cy):
  visitations = []
  for row in grid:
    visitations.append([])
    for cell in row:
      visitations[-1].append(set())

  cur_dir = 0
  y = sy
  x = sx
  while True:
    if y + offsets[cur_dir][0] < 0 or y + offsets[cur_dir][0] >= len(grid) or x + offsets[cur_dir][1] < 0 or x + offsets[cur_dir][1] >= len(grid[0]):
      return False
    if grid[y + offsets[cur_dir][0]][x + offsets[cur_dir][1]] == '#' or ((y + offsets[cur_dir][0]) == cy and (x + offsets[cur_dir][1]) == cx):
      cur_dir = (cur_dir + 1) % len(offsets)
    else:
      y += offsets[cur_dir][0]
      x += offsets[cur_dir][1]
      if offsets[cur_dir] in visitations[y][x]:
        return True
      visitations[y][x].add(offsets[cur_dir])
      grid[y][x] = 'X'


while True:
  if y + offsets[cur_dir][0] < 0 or y + offsets[cur_dir][0] >= len(grid) or x + offsets[cur_dir][1] < 0 or x + offsets[cur_dir][1] >= len(grid[0]):
    break
  if grid[y + offsets[cur_dir][0]][x + offsets[cur_dir][1]] == '#':
    cur_dir = (cur_dir + 1) % len(offsets)
  else:
    y += offsets[cur_dir][0]
    x += offsets[cur_dir][1]
    grid[y][x] = 'X'

lp_count = 0
for ridx, row in enumerate(grid):
  for cidx, col in enumerate(row):
    if ridx == sy and cidx == sx:
      continue
    if col == 'X':
      if check_loop(cidx, ridx):
        lp_count += 1

print(lp_count)
