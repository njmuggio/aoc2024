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

possible_options = {"": 0}
def count_options(req):
  if req in possible_options:
    return possible_options[req]

  options = 0
  for prefix in {pattern for pattern in possible_patterns if req.startswith(pattern)}:
    if req == prefix:
      options += 1
    else:
      options += count_options(req[len(prefix):])

  possible_options[req] = options

  return options

total_options = 0
for req in requested:
  total_options += count_options(req)

print(total_options)
