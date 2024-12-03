#!/usr/bin/env python3

import sys
import re

pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
inpt = ""
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    inpt += line.strip()


filtered = ""
skip = False
while inpt:
  if inpt.startswith("don't()"):
    skip = True
  if inpt.startswith("do()"):
    skip = False

  if not skip:
    filtered += inpt[0]

  inpt = inpt[1:]

value = 0
for match in pattern.findall(filtered):
  value += int(match[0]) * int(match[1])

print(value)
