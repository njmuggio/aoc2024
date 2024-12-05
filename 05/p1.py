#!/usr/bin/env python3

import sys

class Rule:
  def __init__(self, first, second) -> None:
    self.first = first
    self.second = second

rules = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    if len(line.strip()) == 0:
      break

    first, second = line.strip().split("|")
    first = int(first)
    second = int(second)
    rules.append(Rule(first, second))

  valid_updates = 0
  for line in file:
    pages = [int(p) for p in line.strip().split(",")]
    valid = True

    for idx, page in enumerate(pages):
      remaining = pages[idx+1:]
      for rule in rules:
        if page == rule.second and rule.first in remaining:
          valid = False
          break
      if not valid:
        break
    if valid:
      valid_updates += pages[len(pages) // 2]

print(valid_updates)
