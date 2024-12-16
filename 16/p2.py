#!/usr/bin/env python3

import sys

class Edge:
  def __init__(self, src, dst, cost):
    self.src = src
    self.dst = dst
    self.cost = cost

class Node:
  def __init__(self, x, y, d):
    self.x = x
    self.y = y
    self.d = d
    self.edges = set()
    self.in_edges = set()

grid = []
nodes = set()
start = (-1, -1)
end = (-1, -1)
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for y, line in enumerate(file):
    grid.append([[]] * len(line.strip()))
    for x, c in enumerate(line.strip()):
      if c in (".", "S", "E"):
        new_nodes = [Node(x, y, (0, -1)), Node(x, y, (0, 1)), Node(x, y, (-1, 0)), Node(x, y, (1, 0))]
        new_nodes[0].edges.add(Edge(new_nodes[0], new_nodes[2], 1000))
        new_nodes[0].edges.add(Edge(new_nodes[0], new_nodes[3], 1000))
        new_nodes[1].edges.add(Edge(new_nodes[1], new_nodes[2], 1000))
        new_nodes[1].edges.add(Edge(new_nodes[1], new_nodes[3], 1000))
        new_nodes[2].edges.add(Edge(new_nodes[2], new_nodes[0], 1000))
        new_nodes[2].edges.add(Edge(new_nodes[2], new_nodes[1], 1000))
        new_nodes[3].edges.add(Edge(new_nodes[3], new_nodes[0], 1000))
        new_nodes[3].edges.add(Edge(new_nodes[3], new_nodes[1], 1000))

        grid[y][x] = new_nodes
        nodes.update(new_nodes)

      if c == "S":
        start = (x, y)

      if c == "E":
        end = (x, y)

for y, row in enumerate(grid):
  for x, local_nodes in enumerate(row):
    if len(local_nodes) == 0:
      continue

    for i, node in enumerate(local_nodes):
      if len(grid[y+node.d[1]][x+node.d[0]]):
        node.edges.add(Edge(node, grid[y+node.d[1]][x+node.d[0]][i], 1))

for node in nodes:
  for edge in node.edges:
    edge.dst.in_edges.add(edge)

dist = {}
prev = {}
for node in nodes:
  dist[node] = 2**64-1
  prev[node] = set()

dist[grid[start[1]][start[0]][3]] = 0
visited = [grid[start[1]][start[0]][3]]

while visited:
  visited.sort(key=lambda node: dist[node], reverse=True)
  node = visited.pop()

  for edge in node.edges:
    this_cost = dist[node] + edge.cost
    if this_cost < dist[edge.dst]:
      prev[edge.dst] = {node}
      dist[edge.dst] = this_cost
      visited.append(edge.dst)
    elif this_cost == dist[edge.dst]:
      prev[edge.dst].add(node)

frontier = set()
end_nodes = sorted(grid[end[1]][end[0]], key=lambda node: dist[node])
frontier = {end_nodes[0]}
for end_node in end_nodes[1:]:
  if dist[end_node] == dist[end_nodes[0]]:
    frontier.add(end_node)

best_path_nodes = {end}
while frontier:
  node = frontier.pop()
  best_path_nodes.update(((p.x, p.y) for p in prev[node]))
  frontier.update(prev[node])

print(len(best_path_nodes))
