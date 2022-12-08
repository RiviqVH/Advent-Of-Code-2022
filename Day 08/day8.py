### Setup: ###
import os
import numpy as np

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 08")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
grid = np.matrix([[int(y) for y in list(x)] for x in input])
grid_x = grid.shape[0]
grid_y = grid.shape[1]

total_visible = 2*grid_x + 2*grid_y - 4

for x in range(grid_x):
    for y in range(grid_y):
        if x == 0 or y == 0 or x == grid_x-1 or y == grid_y-1:
            continue

        current_val = grid[x,y]

        left = grid[x,0:y] >= current_val
        right = grid[x,y+1:grid_y] >= current_val
        top = grid[0:x,y] >= current_val
        bottom = grid[x+1:grid_x, y] >= current_val

        if left.any() and right.any() and top.any() and bottom.any():
            continue

        total_visible += 1

### Part 2: ###


def one_side_view(current, ordered_list):
    view_count = 0
    for i in ordered_list:
        view_count += 1
        if i >= current:            
            break

    return(view_count)

max_scenic_score = 0
for x in range(grid_x):
    for y in range(grid_y):
        if x == 0 or y == 0 or x == grid_x-1 or y == grid_y-1:
            continue

        current_val = grid[x,y]

        left = grid[x,0:y].tolist()[0][::-1]
        right = grid[x,y+1:grid_y].tolist()[0]
        top = grid[0:x,y].transpose().tolist()[0][::-1]
        bottom = grid[x+1:grid_x, y].transpose().tolist()[0]

        scenic_score = one_side_view(current_val, left) * one_side_view(current_val, right) * one_side_view(current_val, top) * one_side_view(current_val, bottom)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
