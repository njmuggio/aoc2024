#!/usr/bin/env python3

import sys

class Bot:
  def __init__(self, px, py, vx, vy):
    self.px = px
    self.py = py
    self.vx = vx
    self.vy = vy

  def step(self, w, h):
    self.px += self.vx
    self.py += self.vy
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

w = 101
h = 103
#w = 11
#h = 7

def print_grid():
  print("=" * w)
  for row in range(h):
    for col in range(w):
      has_bot = any(bot.px == col and bot.py == row for bot in bots)
      if has_bot:
        print("@", end="")
      else:
        print(" ", end="")
    print()

  print(secs)

secs = 0
while True:
  secs += 1
  for bot in bots:
    bot.step(w, h)

  for bot in bots:
    for off in range(5):
      if not any(other.px == bot.px + off and other.py == bot.px + off for other in bots):
        break
    else:
      print_grid()
      break
