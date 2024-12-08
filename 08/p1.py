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
    anti1 = (first.x - offx, first.y - offy)
    if 0 <= anti1[0] <= width and 0 <= anti1[1] <= height:
      antinodes.add(anti1)
    anti2 = (second.x + offx, second.y + offy)
    if 0 <= anti2[0] <= width and 0 <= anti2[1] <= height:
      antinodes.add(anti2)

print(len(antinodes))
