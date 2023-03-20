import math

with open('inputs/day06.txt', 'r') as file:
    memory = [int(n) for n in file.readline().split()]

SIZE = len(memory)

to_string = lambda a: '-'.join([str(n) for n in a])
seen_configs = set()
cycles = 0

def redistribute() -> str:
    max_element_index = max(enumerate(memory), key=lambda x: x[1])[0]
    starting_value = memory[max_element_index]
    distribution = int(math.ceil(starting_value / SIZE))
    memory[max_element_index] = 0
    i = max_element_index + 1
    while starting_value > 0:
        i %= SIZE
        memory[i] += min(distribution, starting_value)
        starting_value -= distribution
        i += 1
    return to_string(memory)

while True:
    cycles += 1
    current_config = redistribute()
    if current_config in seen_configs:
        break
    seen_configs.add(current_config)

result = cycles
print(f'Day 6 Part 1: It took us {result} redistribution cycles to see the same config twice.\n')    