#!/usr/bin/env python3

import sys

possible_patterns = set()
requested = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  patterns = file.readline().strip().split(", ")

  for pattern in patterns:
    possible_patterns.add(pattern)

  file.readline()

  for line in file:
    requested.append(line.strip())

impossible_patterns = set()
def is_possible(req):
  if req in impossible_patterns:
    return False

  if req in possible_patterns:
    return True

  for prefix in sorted({pattern for pattern in possible_patterns if req.startswith(pattern)}, key=lambda p: len(p), reverse=True):
    if is_possible(req[len(prefix):]):
      possible_patterns.add(req)
      return True

  impossible_patterns.add(req)
  return False

possible = 0
for req in requested:
  if is_possible(req):
    possible += 1

print(possible)
