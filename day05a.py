with open('inputs/day05.txt', 'r') as file:
    offsets = [int(n) for n in file.readlines()]

length = len(offsets)
pos, steps = 0, 0

while pos < length:
    prev = pos
    pos += offsets[pos]
    steps += 1
    offsets[prev] += 1 
    
result = steps
print(f'Day 5 Part 1: It took us {result} steps to reach the end of the maze.\n')