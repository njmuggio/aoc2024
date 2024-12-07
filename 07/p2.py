#!/usr/bin/env python3

import sys

def add(a, b):
  return a + b

def mul(a, b):
  return a * b

def cat(a, b):
  return int(str(a) + str(b))

total = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    parts = line.strip().split()
    goal = int(parts[0][:-1])
    operands = [int(o) for o in parts[1:]]

    operator_mask = 0

    for operator_mask in range(3 ** (len(operands) - 1)):
      operators = []
      for op_sel in range(len(operands) - 1):
        if operator_mask % 3 == 0:
          operators.append(add)
        elif operator_mask % 3 == 1:
          operators.append(mul)
        else:
          operators.append(cat)
        operator_mask = operator_mask // 3

      value = operands[0]
      for next_val, operator in zip(operands[1:], operators):
        value = operator(value, next_val)

      if value == goal:
        total += value
        break

print(total)
