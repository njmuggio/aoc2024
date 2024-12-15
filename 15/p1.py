#!/usr/bin/env python3

import sys

grid = []
inst = []
bot = (-1, -1)
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    if len(line.strip()) == 0:
      break

    if "@" in line:
      bot = (line.find("@"), len(grid))
      line.replace("@", ".")

    grid.append([c for c in line.strip()])

  for line in file:
    inst += [c for c in line.strip()]

def move(x, y):
  global bot
  bx, by = bot
  if grid[by + y][bx + x] == "#":
    return

  if grid[by + y][bx + x] == ".":
    bot = (bx + x, by + y)
    return

  offset = 1
  while grid[by + y * offset][bx + x * offset] == "O":
    offset += 1

  if grid[by + y * offset][bx + x * offset] == "#":
    return

  grid[by + y * offset][bx + x * offset] = "O"
  grid[by + y][bx + x] = "."
  bot = (bx + x, by + y)

for d in inst:
  match d:
    case ">":
      move(1, 0)
    case "<":
      move(-1, 0)
    case "v":
      move(0, 1)
    case "^":
      move(0, -1)

coord_total = 0
for y, row in enumerate(grid):
  for x, col in enumerate(row):
    if col == "O":
      coord_total += y * 100 + x

print(coord_total)
