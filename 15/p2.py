#!/usr/bin/env python3

import sys

class Crate:
  def __init__(self, t, x, y):
    self.t = t
    self.x = x
    self.y = y


inst = []
bot = (-1, -1)
obstacles = set()
crates = set()
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for row_num, line in enumerate(file):
    if len(line.strip()) == 0:
      break

    for col_num, c in enumerate(line.strip()):
      match c:
        case "#":
          obstacles.add((col_num * 2, row_num))
          obstacles.add((col_num * 2 + 1, row_num))
        case "O":
          crates.add(Crate("O", col_num * 2, row_num))
        case "@":
          bot = (col_num * 2, row_num)

  for line in file:
    inst += [c for c in line.strip()]

def is_safe_move(crate, x, y):
  if crate is None:
    return True

  if (crate.x + x, crate.y + y) in obstacles or (crate.x + x + 1, crate.y + y) in obstacles:
    return False

  if x == -1:
    other = get_crate_at(crate.x + x, crate.y + y)
    return is_safe_move(other, x, y)
  elif x == 1:
    other = get_crate_at(crate.x + x + 1, crate.y + y)
    return is_safe_move(other, x, y)
  else:
    left = get_crate_at(crate.x + x, crate.y + y)
    right = get_crate_at(crate.x + x + 1, crate.y + y)
    return is_safe_move(left, x, y) and is_safe_move(right, x, y)

def do_move(crate, x, y):
  if crate is None:
    return
  if x == -1:
    other = get_crate_at(crate.x + x, crate.y + y)
    do_move(other, x, y)
  elif x == 1:
    other = get_crate_at(crate.x + x + 1, crate.y + y)
    do_move(other, x, y)
  else:
    left = get_crate_at(crate.x + x, crate.y + y)
    right = get_crate_at(crate.x + x + 1, crate.y + y)
    do_move(left, x, y)
    if left != right:
      do_move(right, x, y)

  crate.x += x
  crate.y += y

def get_crate_at(x, y):
  for crate in crates:
    if crate.x <= x <= crate.x + 1 and crate.y == y:
      return crate
  return None

def move(x, y):
  global bot
  if (bot[0] + x, bot[1] + y) in obstacles:
    return

  crate = get_crate_at(bot[0] + x, bot[1] + y)
  if crate:
    if not is_safe_move(crate, x, y):
      return
    do_move(crate, x, y)

  bot = (bot[0] + x, bot[1] + y)

def print_warehouse():
  for row in range(max(o[1] for o in obstacles) + 1):
    for col in range(max(o[0] for o in obstacles) + 1):
      if (col, row) in obstacles:
        print("#", end="")
      elif crate := get_crate_at(col, row):
        if col == crate.x:
          print("[", end="")
        else:
          print("]", end="")
      elif (col, row) == bot:
        print("@", end="")
      else:
        print(".", end="")
    print()

#print("Initial state:")
#print_warehouse()
#print()

for d in inst:
  match d:
    case ">":
      move(1, 0)
    case "<":
      move(-1, 0)
    case "v":
      move(0, 1)
    case "^":
      move(0, -1)

  #print("Move", d)
  #print_warehouse()
  #print()

total_coord = 0
for crate in crates:
  total_coord += crate.y * 100 + crate.x

print(total_coord)
