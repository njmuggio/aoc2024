#!/usr/bin/env python3

import sys

class Node:
  def __init__(self, freq, x, y):
    self.freq = freq
    self.x = x
    self.y = y

nodes = set()

height = 0
width = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for y, line in enumerate(file):
    for x, char in enumerate(line.strip()):
      if char != '.':
        nodes.add(Node(char, x, y))

  height = y
  width = x

antinodes = set()
for first in nodes:
  other_matches = {node for node in nodes if node.freq == first.freq and node != first}
  for second in other_matches:
    offx = second.x - first.x
    offy = second.y - first.y
    i = 0
    while True:
      anti = (first.x - offx * i, first.y - offy * i)
      if 0 <= anti[0] <= width and 0 <= anti[1] <= height:
        antinodes.add(anti)
        i += 1
      else:
        break

    i = 0
    while True:
      anti = (second.x + offx * i, second.y + offy * i)
      if 0 <= anti[0] <= width and 0 <= anti[1] <= height:
        antinodes.add(anti)
        i += 1
      else:
        break

print(len(antinodes))
