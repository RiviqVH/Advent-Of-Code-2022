### Setup: ###
import os
import math

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 10")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
cycle = 0
value = 1
result_list = [value]
for r in input:
    match r[:4]:
        case 'noop':
            cycle += 1
            result_list.append(value)
            # print('Input: ' + r + ', cycle: ' + str({'cycle': cycle, 'value': value}))
        case 'addx':
            for i in range(1,3):
                cycle += 1
                result_list.append(value)
                # print('Input: ' + r + ', cycle: ' + str({'cycle': cycle, 'value': value}))
            value += int(r.split(' ')[1])
            # print('addx')

result = 0

for y in [20, 60, 100, 140, 180, 220]:
    result += y * result_list[y]

### Part 2: ###
x_values = result_list[1:]
current_string = ''
row_list = []
for cycle, x in enumerate(x_values):
    if cycle % 40 == 0:
        row_list.append(current_string)
        current_string = ''

    sprite = list(range(x-1, x+2))
    print('Current cycle: ' + str(cycle) + ', printing pixel ' + str(cycle%40) + ' on row ' + str(math.floor(cycle / 40)+1))

    if (cycle % 40) in sprite:
        current_string += '#'
    else:
        current_string += '.'
row_list.append(current_string)

for r in row_list:
    print(r)