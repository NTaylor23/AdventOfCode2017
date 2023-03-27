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

in_infinite_loop = False
loop_start = ''

while True:
    current_config = redistribute()

    if in_infinite_loop:
        cycles += 1
        if current_config == loop_start and cycles > 1:
            break
    else:
        if current_config in seen_configs:
            in_infinite_loop = True
            loop_start = current_config
        seen_configs.add(current_config)

result = cycles
print(f'Day 6 Part 2: The infinite loop is {result} cycles long.\n')