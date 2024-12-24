#!/usr/bin/env python3

import sys

class Const:
  def __init__(self, value):
    self.value = value

  def resolve(self, gates):
    self.value = int(self.value)

  def get(self):
    return self.value

class And:
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def resolve(self, gates):
    self.left = gates[self.left]
    self.right = gates[self.right]

  def get(self):
    return self.left.get() & self.right.get()

class Or:
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def resolve(self, gates):
    self.left = gates[self.left]
    self.right = gates[self.right]

  def get(self):
    return self.left.get() | self.right.get()

class Xor:
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def resolve(self, gates):
    self.left = gates[self.left]
    self.right = gates[self.right]

  def get(self):
    return self.left.get() ^ self.right.get()

gates = {}
high_z = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for line in file:
    if len(line.strip()) == 0:
      break

    parts = line.strip().split(": ")
    gates[parts[0]] = Const(parts[1])

  for line in file:
    parts = line.strip().split()
    left = parts[0]
    type_ = parts[1]
    right = parts[2]
    dest = parts[4]
    match type_:
      case "AND":
        gates[dest] = And(left, right)
      case "OR":
        gates[dest] = Or(left, right)
      case "XOR":
        gates[dest] = Xor(left, right)

    if dest[0] == "z":
      z = int(dest[1:])
      high_z = max(high_z, z)

for gate in gates.values():
  gate.resolve(gates)

result = 0
for z in range(high_z + 1):
  result |= gates[f"z{z:02}"].get() << z

print(result)
