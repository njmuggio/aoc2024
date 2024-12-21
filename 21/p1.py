#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  codes = [line.strip() for line in file]

def offx_char(offx):
  return "<" if offx < 0 else ">"

def offy_char(offy):
  return "^" if offy < 0 else "v"

def paths(code, keypad):
  cur_pos = keypad["A"]
  press_seqs = [""]

  for c in code:
    if keypad[c] == cur_pos:
      # No movement required
      press_seqs = [path + "A" for path in press_seqs]
    else:
      # Some movement required
      curx, cury = cur_pos
      destx, desty = keypad[c]
      offx = destx - curx
      offy = desty - cury
      if offx == 0:
        # Only vertical movement
        addition = abs(offy) * offy_char(offy)
        press_seqs = [path + addition + "A" for path in press_seqs]
      elif offy == 0:
        # Only horizontal movement
        addition = abs(offx) * offx_char(offx)
        press_seqs = [path + addition + "A" for path in press_seqs]
      else:
        # Horizontal and vertical. We need to avoid empty cells, so there may only be one valid option
        new_seqs = []

        # Can we move vertically first?
        if (cur_pos[0], cur_pos[1] + offy) in keypad.values():
          addition = abs(offy) * offy_char(offy)
          addition += abs(offx) * offx_char(offx)
          new_seqs += [path + addition + "A" for path in press_seqs]

        # Can we move horizontally first?
        if (cur_pos[0] + offx, cur_pos[1]) in keypad.values():
          addition = abs(offx) * offx_char(offx)
          addition += abs(offy) * offy_char(offy)
          new_seqs += [path + addition + "A" for path in press_seqs]

        press_seqs = new_seqs

    cur_pos = keypad[c]

  return press_seqs

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
  bot0_paths = set(paths(code, keypad))
  bot1_paths = set()
  for path in bot0_paths:
    bot1_paths.update(paths(path, dpad))

  manual_paths = set()
  for path in bot1_paths:
    manual_paths.update(paths(path, dpad))

  complexity += int(code[:-1]) * len(min(manual_paths, key=lambda p: len(p)))

print(complexity)
