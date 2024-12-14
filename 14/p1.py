#!/usr/bin/env python3

import sys

class Bot:
  def __init__(self, px, py, vx, vy):
    self.px = px
    self.py = py
    self.vx = vx
    self.vy = vy

  def step(self, steps, w, h):
    self.px += self.vx * steps
    self.py += self.vy * steps
    self.px %= w
    self.py %= h

bots = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    parts = line.split()
    p = parts[0].split(",")
    px = int(p[0][2:])
    py = int(p[1])
    v = parts[1].split(",")
    vx = int(v[0][2:])
    vy = int(v[1])
    bots.append(Bot(px, py, vx, vy))

secs = 100
w = 101
h = 103
#w = 11
#h = 7
for bot in bots:
  bot.step(secs, w, h)

q = [[0, 0], [0, 0]]
for bot in bots:
  if bot.px < w // 2:
    x = 0
  elif bot.px > w // 2:
    x = 1
  else:
    continue

  if bot.py < h // 2:
    y = 0
  elif bot.py > h // 2:
    y = 1
  else:
    continue

  q[x][y] += 1

print(q[0][0] * q[0][1] * q[1][0] * q[1][1])
