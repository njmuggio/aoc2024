#!/usr/bin/env python3

import sys

reg_a = 0
reg_b = 0
reg_c = 0
pc = 0
mem = []
output = []

def combo(addr):
  match mem[addr]:
    case 0:
      return 0
    case 1:
      return 1
    case 2:
      return 2
    case 3:
      return 3
    case 4:
      return reg_a
    case 5:
      return reg_b
    case 6:
      return reg_c
  return 0

def adv():
  global reg_a
  global pc
  reg_a = reg_a // 2**combo(pc+1)
  return True

def bxl():
  global reg_b
  global pc
  reg_b = reg_b ^ mem[pc+1]
  return True

def bst():
  global reg_b
  global pc
  reg_b = combo(pc+1) % 8
  return True

def jnz():
  global reg_a
  global pc
  if reg_a != 0:
    pc = mem[pc+1]
    return False
  return True

def bxc():
  global reg_b
  global reg_c
  reg_b = reg_b ^ reg_c
  return True

def out():
  global output
  output.append(combo(pc+1))
  return True

def bdv():
  global reg_b
  global pc
  reg_b = reg_a // 2**combo(pc+1)
  return True

def cdv():
  global reg_c
  global pc
  reg_c = reg_a // 2**combo(pc+1)
  return True

ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  line = file.readline()
  reg_a = int(line.split()[2])
  line = file.readline()
  reg_b = int(line.split()[2])
  line = file.readline()
  reg_c = int(line.split()[2])

  file.readline()

  line = file.readline()
  prog_text = line.split()[1]
  mem = [int(w) for w in prog_text.split(",")]

while pc < len(mem):
  if ops[mem[pc]]():
    pc += 2

print(",".join(str(o % 8) for o in output))
