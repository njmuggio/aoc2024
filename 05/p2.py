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

  invalid_updates = []
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
    if not valid:
      invalid_updates.append(pages)

def fix_single(rules, update):
  for idx in range(len(update)):
    for rule in rules:
      if rule.second == update[idx]:
        try:
          first = update[idx+1:].index(rule.first) + idx + 1
          update[idx] = rule.first
          update[first] = rule.second
          return True
        except:
          pass
  return False

for update in invalid_updates:
  while fix_single(rules, update):
    pass

tot = 0
for update in invalid_updates:
  tot += update[len(update) // 2]

print(tot)
