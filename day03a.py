import math

INPUT   = 347991
COMPASS = [1, -1j, -1, 1j] # Right, Up, Left, Down

length = math.ceil(math.sqrt(INPUT)) 
if length % 2 == 0:
    length += 1

pt = complex(length // 2, length // 2) # [x, y] point
start = pt # start point
num_steps, n, direction = 1, 1, 0

def move(steps_before_rotation: int) -> None:
    global pt, n
    for _ in range(steps_before_rotation):
        if n == INPUT:
            return
        pt += COMPASS[direction]
        n += 1
        
def rotate() -> None:
    global direction
    direction = (direction + 1) % 4

while n < INPUT:
    for _ in range(2):
        move(num_steps)
        rotate()
    num_steps += 1

# Manhattan distance between reached point (where `INPUT` value would be) and start point
result = int(abs(pt.real - start.real) + abs(pt.imag - start.imag)) 
print(f'Day 3 Part 1: {result} steps are needed to carry the data to the access port.\n')