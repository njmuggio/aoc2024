#!/usr/bin/env python3

import sys

class Node:
  def __init__(self, label):
    self.label = label

    self.neighbors = set()

  def is_neighbor(self, other_label):
    for neighbor in self.neighbors:
      if neighbor.label == other_label:
        return True
    return False


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
  inbound_edges = {primary_label: len(primary.neighbors)}
  for n1 in primary.neighbors:
    inbound_edges[n1.label] = 1
    for n2 in primary.neighbors:
      if n1.is_neighbor(n2.label):
        inbound_edges[n1.label] += 1

  skip = False
  while any(edges != inbound_edges[primary_label] for edges in inbound_edges.values()):
    to_strike = min(inbound_edges.keys(), key=lambda label: inbound_edges[label])
    if to_strike == primary_label:
      skip = True
      break
    del inbound_edges[to_strike]
    inbound_edges[primary_label] -= 1
    for neighbor in primary.neighbors:
      if neighbor.label in inbound_edges and n2.is_neighbor(to_strike):
        inbound_edges[neighbor.label] -= 1

  if not skip:
    groups.add(tuple(sorted(inbound_edges.keys())))

largest = max(groups, key=lambda g: len(g))
print(",".join(largest))
