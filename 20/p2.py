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
tiles = []
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
tiles.append(start)
while True:
  for off in ((0, -1), (0, 1), (-1, 0), (1, 0)):
    other_tile = grid[cur_tile.y+off[1]][cur_tile.x+off[0]]
    if other_tile is not None and other_tile.nom_time < 0:
      other_tile.nom_time = cur_tile.nom_time + 1
      cur_tile = other_tile
      break

  tiles.append(cur_tile)
  if cur_tile == end:
    break

time_save_req = 100
cheat_dur = 20
long_cheats = 0
for cheat_start in tiles:
  for cheat_end in tiles[cheat_start.nom_time + time_save_req:]:
    cheat_dist = abs(cheat_end.x - cheat_start.x) + abs(cheat_end.y - cheat_start.y)
    if cheat_dist <= cheat_dur and cheat_end.nom_time - cheat_start.nom_time - cheat_dist >= time_save_req:
      long_cheats += 1

print(long_cheats)
