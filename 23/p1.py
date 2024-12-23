#!/usr/bin/env python3

import sys

class Node:
  def __init__(self, label):
    self.label = label

    self.neighbors = set()


nodes = {}
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    a, b = line.strip().split("-")

    if a not in nodes:
      nodes[a] = Node(a)
    node_a = nodes[a]

    if b not in nodes:
      nodes[b] = Node(b)
    node_b = nodes[b]

    node_a.neighbors.add(node_b)
    node_b.neighbors.add(node_a)

groups = set()
for primary_label, primary in nodes.items():
  for neighbor in primary.neighbors:
    for neighbor_neighbor in neighbor.neighbors:
      if neighbor_neighbor == neighbor or neighbor_neighbor == primary:
        continue
      if neighbor_neighbor in primary.neighbors:
        groups.add(tuple(sorted((primary.label, neighbor.label, neighbor_neighbor.label))))

groups = {group for group in groups if group[0][0] == 't' or group[1][0] == 't' or group[2][0] == 't'}
print(len(groups))
