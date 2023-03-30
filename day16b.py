import numpy as np

def spin(programs: np.ndarray, x: int):
    return np.roll(programs, x)

def exchange(programs: np.ndarray, a: int, b: int):
    programs[[a, b]] = programs[[b, a]]
    return programs

def partner(programs: np.ndarray, a: int, b: int):
    positions = np.where((programs == a) | (programs == b))
    return exchange(programs, positions[0][0], positions[0][1])

with open('inputs/day16.txt', 'r') as file:
    instructions = [inst for inst in file.readline().split(',')]

programs = np.arange(ord('a'), ord('p') + 1, 1, np.int32)
length = len(programs)

"""
Running the program over and over again, we'll get a repeated pattern once we've ran it N times.
Find the pattern at 1,000,000,000 % N to get the final state.
"""
pattern_size = 0
seen = []

while True:
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

    if seen and np.array_equiv(programs, seen[0]):
        break

    pattern_size += 1
    seen.append(programs.copy())

result = ''.join([chr(x) for x in seen[(10**9 % pattern_size) - 1]])
print(f'Day 16 Part 2: After doing their dance 1 billion(!) times, the programs are standing in the order -> {result}.\n')