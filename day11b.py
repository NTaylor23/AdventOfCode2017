from functools import reduce

with open("inputs/day11.txt") as file:
    directions = [direction for direction in file.readline().split(",")]

coordinates = {
    "n": [1, 0, -1],
    "ne": [0, 1, -1],
    "se": [-1, 1, 0],
    "s": [-1, 0, 1],
    "sw": [0, -1, 1],
    "nw": [1, -1, 0],
}

p = [0, 0, 0]
result = 0
for d in directions:
    p = reduce(lambda a, b: [x + y for x, y in zip(a, b)], [p, coordinates[d]])
    result = max(result, max(abs(n) for n in p))

print(f"Day 11 Part 2: The furthest the target ever got on the hex grid is {result}.\n")