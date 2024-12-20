#!/usr/bin/env python3

import sys

class Tile:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.nom_time = -1

    self.prev = None
    self.next = None

grid = []
tiles = set()
#walls = set()
start = None
end = None
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for y, line in enumerate(file):
    grid.append([])
    for x, c in enumerate(line.strip()):
      match c:
        case "#":
          #walls.add((x, y))
          grid[y].append(None)
        case ".":
          grid[y].append(Tile(x, y))
        case "S":
          grid[y].append(Tile(x, y))
          grid[y][-1].nom_time = 0
          start = grid[y][-1]
        case "E":
          grid[y].append(Tile(x, y))
          end = grid[y][-1]

cur_tile = start
while True:
  for off in ((0, -1), (0, 1), (-1, 0), (1, 0)):
    other_tile = grid[cur_tile.y+off[1]][cur_tile.x+off[0]]
    if other_tile is not None and other_tile.nom_time < 0:
      other_tile.nom_time = cur_tile.nom_time + 1
      cur_tile = other_tile
  
  if cur_tile == end:
    break

long_cheats = 0
for y, row in enumerate(grid):
  for x, tile in enumerate(row):
    if tile is None:
      continue

    for off in ((0, -1), (0, 1), (-1, 0), (1, 0)):
      if x + 2 * off[0] < 0 or x + 2 * off[0] >= len(row) or y + 2 * off[1] < 0 or y + 2 * off[1] >= len(grid):
        continue

      if grid[y + off[1]][x + off[0]] is None:
        dest = grid[y + 2 * off[1]][x + 2 * off[0]]
        if dest is not None:
          if dest.nom_time - grid[y][x].nom_time > 101:
            long_cheats += 1

print(long_cheats)
