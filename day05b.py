import numpy as np
from cython_files import process_offsets_cy

with open('inputs/day05.txt', 'r') as file:
    offsets = [int(n) for n in file.readlines()]
    offsets = np.array(offsets, dtype=np.int64)

result = process_offsets_cy.process_offsets(offsets)
print(f'Day 5 Part 2: It took us {result} steps to reach the end of the maze \
with our peculiar new rules.\n') 