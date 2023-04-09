values, instructions = {}, {}
sounds = []

with open('inputs/day18.txt', 'r') as file:
    for idx, line in enumerate(file.readlines()):
        command, *vars = line.split()
        values[vars[0]] = 0
        instructions[idx] = [command, vars]
        
def get_value(y) -> input:
    if not y.strip('-').isnumeric():
        return values[y]
    return int(y)

operation_map = {
        'set': lambda x, y: values.__setitem__(x, y),
        'add': lambda x, y: values.__setitem__(x, values[x] + y),
        'mul': lambda x, y: values.__setitem__(x, values[x] * y),
        'mod': lambda x, y: values.__setitem__(x, values[x] % y),
    }

idx = 0
while idx < len(instructions):
    current_line = instructions[idx]
    inst, x = current_line[0], current_line[1][0]
    
    if len(current_line[1]) > 1:
        y = current_line[1][1] 
    
    if inst == 'rcv' and get_value(x) != 0:
        # Terminating condition
        break
    elif inst == 'snd':
        sounds.append(get_value(x))
    elif inst == 'jgz' and get_value(x) > 0:
        idx += get_value(y)
        continue
    elif inst in operation_map: # set, add, multiply or modulo
        y = get_value(y)
        operation_map[inst](x, y)
    idx += 1

result = sounds[-1]
print(f'Day 18 Part 1: The value of the recovered frequency the first time a `rcv` instruction appears is {result}.\n')
