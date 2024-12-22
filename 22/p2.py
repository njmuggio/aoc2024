#!/usr/bin/env python3

import sys

def build_signal_map(seed, iters):
  cost_history = [None, None, None, None, seed % 10]
  signal_map = {}
  for i in range(iters):
    seed = (seed ^ (seed << 6)) & 0xFFFFFF
    seed = ((seed >> 5) ^ seed) & 0xFFFFFF
    seed = ((seed << 11) ^ seed) & 0xFFFFFF
    
    cost_history[0] = cost_history[1]
    cost_history[1] = cost_history[2]
    cost_history[2] = cost_history[3]
    cost_history[3] = cost_history[4]
    cost_history[4] = seed % 10

    if i >= 3 and seed % 10 > 0:
      a = cost_history[1] - cost_history[0]
      b = cost_history[2] - cost_history[1]
      c = cost_history[3] - cost_history[2]
      d = cost_history[4] - cost_history[3]
      if a not in signal_map:
        signal_map[a] = {}
      if b not in signal_map[a]:
        signal_map[a][b] = {}
      if c not in signal_map[a][b]:
        signal_map[a][b][c] = {}
      if d not in signal_map[a][b][c]:
        signal_map[a][b][c][d] = seed % 10
  return signal_map

signal_maps = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    signal_maps.append(build_signal_map(int(line.strip()), 2000))

max_profit = 0

for a in range(-10, 11):
  for b in range(-10, 11):
    for c in range(-10, 11):
      for d in range(-10, 11):
        this_profit = 0
        for signal_map in signal_maps:
          try:
            this_profit += signal_map[a][b][c][d]
          except:
            pass

        if this_profit > max_profit:
          max_profit = this_profit

print(max_profit)
