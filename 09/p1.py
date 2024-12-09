#!/usr/bin/env python3

import sys

class Block:
  def __init__(self, file_id, pos, size, file_pos):
    self.file_id = file_id
    self.pos = pos
    self.size = size
    self.file_pos = file_pos

    self.used = 0

  def use(self):
    self.used += 1

  def end(self):
    assert self.used == self.size

disk = []
next_id = 0
pos = 0
is_file = True
total_file_size = 0
file_blocks = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for c in file.readline().strip():
    size = int(c)
    if is_file:
      if size != 0:
        disk.append(Block(next_id, pos, size, total_file_size))
      file_blocks.append(disk[-1])
      next_id += 1
      total_file_size += size
    else:
      if size != 0:
        disk.append(Block(-1, pos, int(c), total_file_size))

    pos += size
    is_file = not is_file

from_start = 0
from_end = total_file_size - 1
cur_block_idx = 0

checksum = 0

def find_block_from_start(offset):
  cur_file_offset = 0
  for block in file_blocks:
    if cur_file_offset <= offset < cur_file_offset + block.size:
      return block
    cur_file_offset += block.size

def find_block_from_end(offset):
  for block in reversed(file_blocks):
    if block.file_pos <= offset < block.file_pos + block.size:
      return block
    else:
      block.end()

for i in range(total_file_size):
  cur_block = disk[cur_block_idx]

  if i == cur_block.pos + cur_block.size:
    cur_block_idx += 1
    cur_block = disk[cur_block_idx]

  if cur_block.file_id >= 0:
    checksum += i * cur_block.file_id
    from_start += 1
    cur_block.use()
  else:
    checksum += i * find_block_from_end(from_end).file_id
    find_block_from_end(from_end).use()
    from_end -= 1

for block in file_blocks:
  block.end()

print(checksum)
