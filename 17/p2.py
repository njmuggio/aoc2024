#!/usr/bin/env python3

import sys

class Vm:
  def __init__(self, mem, a, b, c):
    self.reg_a = a
    self.reg_b = b
    self.reg_c = c
    self.pc = 0
    self.mem = mem
    self.output = []
    self.ops = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]

  def combo(self, addr):
    match self.mem[addr]:
      case 0:
        return 0
      case 1:
        return 1
      case 2:
        return 2
      case 3:
        return 3
      case 4:
        return self.reg_a
      case 5:
        return self.reg_b
      case 6:
        return self.reg_c
      case 7:
        self.pc = len(self.mem)
        return 0

  def adv(self):
    self.reg_a = self.reg_a // 2**self.combo(self.pc+1)
    return True

  def bxl(self):
    self.reg_b = self.reg_b ^ self.mem[self.pc+1]
    return True

  def bst(self):
    self.reg_b = self.combo(self.pc+1) % 8
    return True

  def jnz(self):
    if self.reg_a != 0:
      self.pc = self.mem[self.pc+1]
      return False
    return True

  def bxc(self):
    self.reg_b = self.reg_b ^ self.reg_c
    return True

  def out(self):
    self.output.append(self.combo(self.pc+1) % 8)
    if len(self.output) > len(self.mem):
      self.pc = len(self.mem)
      return True
    for o, e in zip(self.output, self.mem):
      if o != e:
        self.pc = len(self.mem)
        return True
    return True

  def bdv(self):
    self.reg_b = self.reg_a // 2**self.combo(self.pc+1)
    return True

  def cdv(self):
    self.reg_c = self.reg_a // 2**self.combo(self.pc+1)
    return True


  def run(self):
    while self.pc < len(self.mem):
      if self.ops[self.mem[self.pc]]():
        self.pc += 2

    return len(self.output) == len(self.mem) and all(o == e for o, e in zip(self.output, self.mem))

  def reset(self, a, b, c):
    self.reg_a = a
    self.reg_b = b
    self.reg_c = c
    self.output = []
    self.pc = 0

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  line = file.readline()
  init_a = int(line.split()[2])
  line = file.readline()
  init_b = int(line.split()[2])
  line = file.readline()
  init_c = int(line.split()[2])

  file.readline()

  line = file.readline()
  prog_text = line.split()[1]
  init_mem = [int(w) for w in prog_text.split(",")]

a = 0
vm = Vm(init_mem, a, init_b, init_c)
while not vm.run():
  if a & 0xFFFF == 0:
    print(a)
  a += 1
  vm.reset(a, init_b, init_c)

print(a)
