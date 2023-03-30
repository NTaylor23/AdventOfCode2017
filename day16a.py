import numpy as np

def spin(programs: np.ndarray, x: int):
    return np.roll(programs, x)

def exchange(programs: np.ndarray, a: int, b: int):
    programs[[a, b]] = programs[[b, a]]
    return programs

def partner(programs: np.ndarray, a: int, b: int):
    a_pos, b_pos = np.where(programs == a)[0][0], np.where(programs == b)[0][0]
    return exchange(programs, a_pos, b_pos)

with open('inputs/day16.txt', 'r') as file:
    instructions = [inst for inst in file.readline().split(',')]

programs = np.arange(ord('a'), ord('p') + 1, 1, np.int32)
length = len(programs)

for inst in instructions:
    if inst[0] == 's':
        x = int(inst[1:])
        programs = spin(programs, x)
    elif inst[0] == 'x':
        a, b = tuple(inst[1:].split('/'))
        programs = exchange(programs, int(a), int(b))
    else:
        a, b = tuple(inst[1:].split('/'))
        programs = partner(programs, ord(a), ord(b))

result = ''.join([chr(n) for n in programs])
print(f'Day 16 Part 1: After their dance, the programs are standing in the order -> {result}.\n')
