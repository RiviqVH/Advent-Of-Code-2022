### Setup: ###
import os

os.chdir(r'C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 01')

### Read input: ###
with open('input.txt') as f:
    input = f.readlines()

# print(input)

### P1: ###
sum_list = []
current_sum = 0
for l in input:    
    if l == '\n':
        sum_list += [current_sum]
        current_sum = 0
        continue
    current_sum += int(l.rstrip("\n"))

answer1 = max(sum_list)

### P2: ###
sum_list_ordered = sorted(sum_list, reverse=True)
answer2 = sum(sum_list_ordered[:3])