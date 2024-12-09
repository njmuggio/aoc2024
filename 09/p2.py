#!/usr/bin/env python3

import sys

class Block:
  def __init__(self, file_id, pos, size):
    self.file_id = file_id
    self.pos = pos
    self.size = size

disk = []
next_id = 0
pos = 0
is_file = True
file_blocks = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for c in file.readline().strip():
    size = int(c)
    if is_file:
      if size != 0:
        disk.append(Block(next_id, pos, size))
      file_blocks.append(disk[-1])
      next_id += 1
    else:
      if size != 0:
        disk.append(Block(-1, pos, int(c)))

    pos += size
    is_file = not is_file

for block in reversed(file_blocks):
  real_idx = -1
  for didx, dest in enumerate(disk):
    if dest.file_id >= 0:
      continue
    if block.size > dest.size:
      continue
    if block.pos < dest.pos:
      continue
    real_idx = didx
    break
  if real_idx >= 0:
    dest = disk[real_idx]
    new_block = Block(block.file_id, dest.pos, block.size)

    if dest.size == block.size:
      block.file_id = -1
      disk[real_idx] = new_block
    else:
      block.file_id = -1
      dest.pos += block.size
      dest.size -= block.size
      disk.insert(real_idx, new_block)

checksum = 0
for block in disk:
  if block.file_id < 0:
    continue

  local_check = sum(i * block.file_id for i in range(block.pos, block.pos + block.size))
  checksum += local_check

print(checksum)
