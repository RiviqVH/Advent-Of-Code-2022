### Setup: ###
import os

os.chdir(r'C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 02')

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
total_score = 0
for l in input:
    opp = l.split(' ')[0]
    me = l.split(' ')[1]
    match me:
        case 'X':
            total_score += 1
            if opp == 'A':
                total_score += 3
            elif opp == 'B':
                total_score += 0
            elif opp == 'C':
                total_score += 6
        case 'Y':
            total_score += 2
            if opp == 'A':
                total_score += 6
            elif opp == 'B':
                total_score += 3
            elif opp == 'C':
                total_score += 0
        case 'Z':
            total_score += 3
            if opp == 'A':
                total_score += 0
            elif opp == 'B':
                total_score += 6
            elif opp == 'C':
                total_score += 3

print(total_score)

### Part 2: ###
total_score = 0
for l in input:
    opp = l.split(' ')[0]
    me = l.split(' ')[1]
    match me:
        case 'X':
            total_score += 0
            if opp == 'A':
                total_score += 3
            elif opp == 'B':
                total_score += 1
            elif opp == 'C':
                total_score += 2
        case 'Y':
            total_score += 3
            if opp == 'A':
                total_score += 1
            elif opp == 'B':
                total_score += 2
            elif opp == 'C':
                total_score += 3
        case 'Z':
            total_score += 6
            if opp == 'A':
                total_score += 2
            elif opp == 'B':
                total_score += 3
            elif opp == 'C':
                total_score += 1

print(total_score)