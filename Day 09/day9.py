### Setup: ###
import os
from pprint import pprint

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 09")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

print(input)

### Part 1: ###
def move_one(position, direction):    
    match direction:
        case 'U': position[1] += 1
        case 'D': position[1] -= 1
        case 'R': position[0] += 1
        case 'L': position[0] -= 1
        case 'UR': position[0] += 1; position[1] += 1
        case 'UL': position[0] -= 1; position[1] += 1
        case 'DR': position[0] += 1; position[1] -= 1
        case 'DL': position[0] -= 1; position[1] -= 1
    return(position)

def distance(coord1, coord2):
    return([c1 - c2 for (c1, c2) in zip(coord1, coord2)])

H = [0,0]
T = [0,0]
t_list = [(0,0)]
for r in input:
    direction = r.split(' ')[0]
    number = int(r.split(' ')[1])
    for i in range(number):
        H = move_one(H, direction)
        d = distance(H, T)
        print('H moved to ' + str(H) + ', distance: ' + str(d))
        if abs(d[0]) > 1 or abs(d[1]) > 1:
            match d:
                case [0,2]: T = move_one(T, 'U')
                case [0,-2]: T = move_one(T, 'D')
                case [2,0]: T = move_one(T, 'R')
                case [-2,0]: T = move_one(T, 'L')
                case [1,2]: T = move_one(T, 'UR')
                case [1,-2]: T = move_one(T, 'DR')
                case [2,1]: T = move_one(T, 'UR')
                case [-2,1]: T = move_one(T, 'UL')
                case [2,-1]: T = move_one(T, 'DR')
                case [-2,-1]: T = move_one(T, 'DL')
                case [-1,2]: T = move_one(T, 'UL')
                case [-1,-2]: T = move_one(T, 'DL')
            t_list.append(tuple(T))
            print('T moved to ' + str(T))
        else:
            print('T stayed at ' + str(T))
part1 = len(set(t_list))

### Part 2: ###
rope = [[0,0] for i in range(10)]
t_list2 = [(0,0)]
def update_positions(rope, direction):
    H = rope[0]
    for idx, knot in enumerate(rope):
        if idx == 0:
            knot = move_one(knot, direction)
            print('H moved to ' + str(knot))
            continue
        d = distance(rope[idx-1], knot)
        if abs(d[0]) + abs(d[1]) > 3: print('Weird distance found: ' + str(d))
        # print('Distance between knot ' + str(idx -1) + ' and ' + str(idx) + ' = ' + str(d))
        if abs(d[0]) > 1 or abs(d[1]) > 1:
            match d:
                case [0,2]: knot = move_one(knot, 'U')
                case [0,-2]: knot = move_one(knot, 'D')
                case [2,0]: knot = move_one(knot, 'R')
                case [-2,0]: knot = move_one(knot, 'L')
                case [1,2]: knot = move_one(knot, 'UR')
                case [1,-2]: knot = move_one(knot, 'DR')
                case [2,1]: knot = move_one(knot, 'UR')
                case [-2,1]: knot = move_one(knot, 'UL')
                case [2,-1]: knot = move_one(knot, 'DR')
                case [-2,-1]: knot = move_one(knot, 'DL')
                case [-1,2]: knot = move_one(knot, 'UL')
                case [-1,-2]: knot = move_one(knot, 'DL')
                case [-2,-2]: knot = move_one(knot, 'DL')
                case [-2,2]: knot = move_one(knot, 'UL')
                case [2,-2]: knot = move_one(knot, 'DR')
                case [2,2]: knot = move_one(knot, 'UR')
            if(idx == 9): t_list2.append(tuple(knot))
            # print('Knot ' + str(idx) + ' moved to ' + str(knot))
        # else:
        #     print(('Knot ' + str(idx) + ' stayed at ' + str(knot)))

for r in input:
    print(r)
    direction = r.split(' ')[0]
    number = int(r.split(' ')[1])
    for i in range(number):
        update_positions(rope, direction)

part2 = len(set(t_list2))
