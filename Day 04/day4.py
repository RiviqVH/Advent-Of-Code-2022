### Setup: ###
import os

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 04")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
p1_total = 0
for l in input:
    A = l.split(',')[0].split('-')
    B = l.split(',')[1].split('-')

    A_set = set(range(int(A[0]), int(A[1]) + 1))
    B_set = set(range(int(B[0]), int(B[1]) + 1))

    lengths = [len(A_set), len(B_set)]

    if len(set.intersection(A_set, B_set)) == min(lengths):
        p1_total += 1

### Part 2: ###
p2_total = 0
for l in input:
    A = l.split(',')[0].split('-')
    B = l.split(',')[1].split('-')

    A_set = set(range(int(A[0]), int(A[1]) + 1))
    B_set = set(range(int(B[0]), int(B[1]) + 1))

    lengths = [len(A_set), len(B_set)]

    if len(set.intersection(A_set, B_set)) > 0:
        p2_total += 1