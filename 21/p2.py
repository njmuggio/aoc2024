#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  codes = [line.strip() for line in file]

def offx_char(offx):
  return "<" if offx < 0 else ">"

def offy_char(offy):
  return "^" if offy < 0 else "v"

memo = {i: {} for i in range(26)}

def dpad_code_len(start, end, depth) -> int:
  if (start, end) in memo[depth]:
    return memo[depth][(start, end)]

  sx, sy = dpad[start]
  ex, ey = dpad[end]
  ox = ex - sx
  oy = ey - sy

  def recur(path) -> int:
    if depth == 1:
      return len(path)

    path = "A" + path
    total_len = 0
    for idx in range(len(path) - 1):
      total_len += dpad_code_len(path[idx], path[idx+1], depth - 1)
    return total_len

  if ox == 0 or oy == 0:
    path = abs(oy) * offy_char(oy) + abs(ox) * offx_char(ox) + "A"
    memo[depth][(start, end)] = recur(path)
    return memo[depth][(start, end)]
  else:
    if start == "<":
      # Must move right first
      path = abs(ox) * offx_char(ox) + abs(oy) * offy_char(oy) + "A"
      memo[depth][(start, end)] = recur(path)
      return memo[depth][(start, end)]

    if end == "<":
      # Must move down first
      path = abs(oy) * offy_char(oy) + abs(ox) * offx_char(ox) + "A"
      memo[depth][(start, end)] = recur(path)
      return memo[depth][(start, end)]

    # Need to try both vertical and horizontal first
    vert_path = abs(oy) * offy_char(oy) + abs(ox) * offx_char(ox) + "A"
    vert = recur(vert_path)

    horiz_path = abs(ox) * offx_char(ox) + abs(oy) * offy_char(oy) + "A"
    horiz = recur(horiz_path)

    if vert <= horiz:
      memo[depth][(start, end)] = vert
      return vert
    memo[depth][(start, end)] = horiz
    return horiz

def keypad_code_len(code):
  code = "A" + code
  total_len = 0
  depth = 25
  for idx in range(len(code) - 1):
    code_start = code[idx]
    code_end = code[idx+1]

    sx, sy = keypad[code_start]
    ex, ey = keypad[code_end]
    ox = ex - sx
    oy = ey - sy

    if ox == 0 or oy == 0:
      path = "A" + abs(ox) * offx_char(ox) + abs(oy) * offy_char(oy) + "A"
      for pidx in range(len(path) - 1):
        total_len += dpad_code_len(path[pidx], path[pidx+1], depth)
    else:
      horiz_len = 2**64-1
      vert_len = 2**64-1

      # Can we move horizontally first?
      if (sx + ox, sy) in keypad.values():
        path = "A" + abs(ox) * offx_char(ox) + abs(oy) * offy_char(oy) + "A"
        horiz_len = 0
        for pidx in range(len(path) - 1):
          horiz_len += dpad_code_len(path[pidx], path[pidx+1], depth)

      # Can we move vertically first?
      if (sx, sy + oy) in keypad.values():
        path = "A" + abs(oy) * offy_char(oy) + abs(ox) * offx_char(ox) + "A"
        vert_len = 0
        for pidx in range(len(path) - 1):
          vert_len += dpad_code_len(path[pidx], path[pidx+1], depth)

      total_len += min(horiz_len, vert_len)

  return total_len


keypad = {
  "A": (2, 3),
  "0": (1, 3),
  "1": (0, 2),
  "2": (1, 2),
  "3": (2, 2),
  "4": (0, 1),
  "5": (1, 1),
  "6": (2, 1),
  "7": (0, 0),
  "8": (1, 0),
  "9": (2, 0),
}

dpad = {
  "A": (2, 0),
  "^": (1, 0),
  "<": (0, 1),
  "v": (1, 1),
  ">": (2, 1),
}

complexity = 0
for code in codes:
  complexity += int(code[:-1]) * keypad_code_len(code)

print(complexity)
