#!/usr/bin/env python3

import sys

def add(a, b):
  return a + b

def mul(a, b):
  return a * b

total = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    parts = line.strip().split()
    goal = int(parts[0][:-1])
    operands = [int(o) for o in parts[1:]]

    operator_mask = 0

    for operator_mask in range(2 ** (len(operands) - 1)):
      operators = []
      for bit in range(len(operands) - 1):
        if operator_mask & (1 << bit) == 0:
          operators.append(add)
        else:
          operators.append(mul)

      value = operands[0]
      for next_val, operator in zip(operands[1:], operators):
        value = operator(value, next_val)

      if value == goal:
        total += value
        break

print(total)
