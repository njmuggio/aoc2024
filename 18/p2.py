#!/usr/bin/env python3

import sys

class Node:
  def __init__(self):
    self.up = None
    self.down = None
    self.left = None
    self.right = None

  @property
  def neighbors(self):
    ret = set()
    if self.up:
      ret.add(self.up)
    if self.down:
      ret.add(self.down)
    if self.left:
      ret.add(self.left)
    if self.right:
      ret.add(self.right)
    return ret

nodes = set()
grid = []

for y in range(71):
  grid.append([])
  for x in range(71):
    grid[-1].append(Node())
    nodes.add(grid[-1][-1])

for y, row in enumerate(grid):
  for x, node in enumerate(row):
    if y > 0:
      node.up = grid[y-1][x]
    if y < len(grid) - 1:
      node.down = grid[y+1][x]
    if x > 0:
      node.left = grid[y][x-1]
    if x < len(row) - 1:
      node.right = grid[y][x+1]

corrupt_cells = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    x, y = line.strip().split(",")
    corrupt_cells.append((int(x), int(y)))

def steps_to_end():
  dist = {}
  prev = {}
  for node in nodes:
    dist[node] = 2**64-1
    prev[node] = None

  dist[grid[0][0]] = 0
  visited = [grid[0][0]]

  while visited:
    visited.sort(key=lambda node: dist[node], reverse=True)
    node = visited.pop()

    for neighbor in node.neighbors:
      if dist[node] + 1 < dist[neighbor]:
        dist[neighbor] = dist[node] + 1
        prev[neighbor] = node
        visited.append(neighbor)
      if neighbor == grid[70][70]:
        return True

  return False

for idx, cell in enumerate(corrupt_cells):
  node = grid[cell[1]][cell[0]]
  if node.up:
    node.up.down = None
    node.up = None
  if node.down:
    node.down.up = None
    node.down = None
  if node.left:
    node.left.right = None
    node.left = None
  if node.right:
    node.right.left = None
    node.right = None

  if idx >= 1024:
    if not steps_to_end():
      print(f"{cell[0]},{cell[1]}")
      break
