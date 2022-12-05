### Setup: ###
import os

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 05")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
drawing = input[:input.index('')]
rearrangement = input[input.index('')+1:]
n_stacks = int(max(drawing[-1:][0].split(' ')))

# Rearrange into array per stack:
original_crates = [[] for i in range(n_stacks)]
for it, line in enumerate(reversed(drawing[:-1])):
    clean_line = list(line)
    del clean_line[3::4]
    clean_line = ''.join(clean_line)
    for iter, i in enumerate(range(3, len(clean_line)+1, 3)):
        if clean_line[i-3:i] == '   ':
            continue
        original_crates[iter] += [clean_line[i-3:i]]
        
def move1(stacks, frm, to):
    frm -= 1
    to -= 1
    crate = stacks[frm][-1]
    del stacks[frm][-1]
    stacks[to].append(crate)

crates1 = original_crates.copy()
for l in rearrangement:
    n = int(l.split(' ')[1])
    frm = int(l.split(' ')[3])
    to = int(l.split(' ')[5])
    for i in range(n):
        move1(crates1, frm, to)

print([x[-1] for x in crates1])

### Part 2: ###
crates2 = original_crates.copy()
def move2(stacks, frm, to, amnt):
    frm -= 1
    to -= 1
    crates = stacks[frm][-amnt:]
    del stacks[frm][-amnt:]
    for c in crates:
        stacks[to].append(c)

for l in rearrangement:
    n = int(l.split(' ')[1])
    frm = int(l.split(' ')[3])
    to = int(l.split(' ')[5])
    
    move2(crates2, frm, to, n)

print([x[-1] for x in crates2])