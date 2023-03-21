import math
import collections 

INPUT   = 347991
COMPASS = [1, -1j, -1, 1j] # Right, Up, Left, Down
NEIGHBORS = COMPASS + [complex(-1, -1), complex(-1, 1), complex(1, -1), complex(1, 1)] # Add Diagonals

length = math.ceil(math.sqrt(INPUT)) 
if length % 2 == 0:
    length += 1

adj_list = collections.defaultdict(int)
pt = complex(length // 2, length // 2) 
num_steps, n, direction = 1, 1, 0

def check_neighbors(point) -> int:
    sum_of_adjacent_points = 0
    for adjacent_point in NEIGHBORS:
        sum_of_adjacent_points += adj_list[point + adjacent_point]
    return sum_of_adjacent_points

def move(steps_before_rotation: int) -> None:
    global pt, n
    for _ in range(steps_before_rotation):
        n = max(check_neighbors(pt), 1)
        adj_list[pt] = n
        if n > INPUT:
            return
        pt += COMPASS[direction]
        
def rotate() -> None:
    global direction
    direction = (direction + 1) % 4

while n <= INPUT:
    for _ in range(2):
        move(num_steps)
        rotate()
    num_steps += 1

result = n
print(f'Day 3 Part 2: {result} is the first number greater than my puzzle input.\n')