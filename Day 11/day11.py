### Setup: ###
import os
import math

os.chdir(r"C:\Users\Vladimir\Documents\Projects\Riviq\Advent of Code 2022\Day 11")

### Read input: ###
with open('input.txt') as f:
    input = [l.strip('\n') for l in f.readlines()]

# print(input)

### Part 1: ###
def parse_input(input):
    monkeys = {}
    for r in input:
        if r.startswith('Monkey '):
            monkey_counter = int(r[-2])
            monkeys[monkey_counter] = {}
            continue
        
        if 'Starting items: ' in r:
            item_list = [int(x) for x in r.split('Starting items: ')[1].split(', ')]
            monkeys[monkey_counter]['items'] = item_list
            continue

        if 'Operation' in r:
            operation = r.split('new = old ')[1]
            monkeys[monkey_counter]['operation'] = operation
            continue

        if 'Test: ' in r:
            test = r.split('Test: divisible by ')[1]
            monkeys[monkey_counter]['test'] = int(test)
            continue

        if 'If true:' in r:
            test_true = r.split('If true: throw to monkey ')[1]
            monkeys[monkey_counter]['if_true'] = int(test_true)
            continue

        if 'If false: ' in r:
            test_false = r.split('If false: throw to monkey ')[1]
            monkeys[monkey_counter]['if_false'] = int(test_false)
            continue

        if r == '':
            continue
        
    return(monkeys)

def simulation(monkeys, rounds = 20, worry_reduction = True):
    inspection_count = {}
    test_product = math.prod(monkeys[x]['test'] for x in monkeys)
    for round in range(rounds):
        # print('Round ' + str(round+1) + '...')
        for n in monkeys:
            # print('\tMonkey ' + str(n))
            if n not in inspection_count:
                inspection_count[n] = 0
            monkey = monkeys[n]
            for i in monkey['items']:
                # 0: Count # of inspections
                inspection_count[n] += 1

                # 1: Perform worry operation
                if monkey['operation'].split(' ')[0] == '*':
                    if monkey['operation'].split(' ')[1] == 'old':
                        i *= i
                    else:
                        i *= int(monkey['operation'].split(' ')[1])
                elif monkey['operation'].split(' ')[0] == '+':
                    if monkey['operation'].split(' ')[1] == 'old':
                        i += i
                    else:
                        i += int(monkey['operation'].split(' ')[1])

                # 2: Perform worry reduction
                if worry_reduction:
                    i = math.floor(i/3)
                else:
                    i = i % test_product

                # 3: Test worry level & throw item
                if i % monkey['test'] == 0:
                    throw_to = monkey['if_true']
                    monkeys[throw_to]['items'].append(i)
                else:
                    throw_to = monkey['if_false']
                    monkeys[throw_to]['items'].append(i)
                
            # 4: empty item list at end of monkey turn
            monkey['items'] = []
    
    return(inspection_count)

monkeys1 = parse_input(input)
result1 = simulation(monkeys1)
part1 = sorted(list(result1.values()), reverse=True)[0] * sorted(list(result1.values()), reverse=True)[1]

### Part 2: ###
monkeys2 = parse_input(input)
result2 = simulation(monkeys2, rounds=10000, worry_reduction=False)
part2 = sorted(list(result2.values()), reverse=True)[0] * sorted(list(result2.values()), reverse=True)[1]