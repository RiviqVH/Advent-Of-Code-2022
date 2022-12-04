### Setup: ###
import os
import string

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 3")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
p1_score = 0
for l in input:
    compartment1 = set(l[:int(len(l) / 2)])
    compartment2 = set(l[int(len(l) / 2):])

    overlap = compartment1.intersection(compartment2)
    if len(overlap) > 1:
        print(overlap)

    letter = list(overlap)[0]
    p1_score += string.ascii_letters.index(letter) + 1

### Part 2: ###
p2_score = 0
for i in range(3, len(input)+1, 3):
    # print(i)
    group = [set(x) for x in input[(i-3):i]]
    if len(group) != 3: print(group)
    letter = list(set.intersection(group[0], group[1], group[2]))[0]
    # print(letter)
    # if len(letter) != 1: print(len(letter))
    p2_score += string.ascii_letters.index(letter) + 1
