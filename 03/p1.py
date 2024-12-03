#!/usr/bin/env python3

import sys
import re

pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
inpt = ""
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    inpt += line.strip()

value = 0
for match in pattern.findall(inpt):
  value += int(match[0]) * int(match[1])

print(value)
