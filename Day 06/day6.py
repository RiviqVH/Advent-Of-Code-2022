### Setup: ###
import os

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 06")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
signal = input[0]
for c in range(4, len(signal)):
    # print(signal[c-4:c])
    if not (len(set(signal[c-4:c]))) < 4:
        print("Found it: " + signal[c-4:c] + ', @ position ' + str(c))
        break

### Part 2: ###
signal2 = input[0]
for c in range(14, len(signal2)):
    # print(signal[c-4:c])
    if not (len(set(signal2[c-14:c]))) < 14:
        print("Found it: " + signal2[c-14:c] + ', @ position ' + str(c))
        break

### Alternatively:
def find_unique_substring(input, length):
    for c in range(length, len(input)):
        if not (len(set(input[c-length:c]))) < length:
            print("Found it: " + input[c-length:c] + ', @ position ' + str(c))
            break