#!/usr/bin/env python3

import sys

nums = {}

def add(d, num, amt=1):
  if num in d:
    d[num] += amt
  else:
    d[num] = amt

with open(sys.argv[1], mode="rt", encoding="utf-8") as file:
  for num_str in file.readline().split():
    num = int(num_str)
    add(nums, num)

for _ in range(25):
  new_nums = {}

  for num, count in nums.items():
    if num == 0:
      add(new_nums, 1, count)
    else:
      num_str = str(num)
      if len(num_str) % 2 == 0:
        a = int(num_str[:len(num_str) // 2])
        b = int(num_str[len(num_str) // 2:])
        add(new_nums, a, count)
        add(new_nums, b, count)
      else:
        add(new_nums, num * 2024, count)

  nums = new_nums

print(sum(nums.values()))
