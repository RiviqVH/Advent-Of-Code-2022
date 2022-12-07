### Setup: ###
import os

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 07")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
def get_fs(input):
    fs = {}
    current_path = ''

    for l in input:
        if l.startswith('$ cd'):
            current_dir = l.lstrip('$ cd ')
            if current_dir == '..':
                current_path = '/'.join(current_path.split('/')[:-1])
            else:
                current_path += '/' + current_dir
                fs[current_path] = {}
        elif l.startswith('$ ls'):
            continue
        else:
            if l.startswith('dir '):
                continue
            else:
                file_name = l.split(' ')[1]
                size = int(l.split(' ')[0])
                fs[current_path][file_name] = size
    return(fs)

def total_dir_sizes(fs):
    sizes = {}
    for l in fs:
        total_size = 0
        subdirs = {x: fs[x] for x in fs if l in x}
        for d in subdirs:
            total_size += sum(subdirs[d].values())
        sizes[l] = total_size
    return(sizes)

final_fs = get_fs(input)
final_sizes = total_dir_sizes(final_fs)
part1 = sum([final_sizes[x] for x in final_sizes if final_sizes[x] <= 100000])

### Part 2: ###
part2 = min([final_sizes[x] for x in final_sizes if final_sizes[x] >= (30000000 - (70000000 - final_sizes['//']))])