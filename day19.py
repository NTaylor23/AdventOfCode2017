import string
from enum import Enum

class Directions(Enum):
    LEFT  = 0
    RIGHT = 1
    UP    = 2
    DOWN  = 3

with open('inputs/day19.txt', 'r') as file:
    maze = []
    for line in file.readlines():
        maze.append(list(line[:-1]))

B = ' ' # Blank Space
V = '|' # Vertical Movement
H = '-' # Horizontal Movement
J = '+' # Junction
L = set(list(string.ascii_uppercase)) # Letters

MAX_R, MAX_C = len(maze), len(maze[0])

def find_entry_point(maze_row: list) -> tuple:
    for idx, col in enumerate(maze_row):
        if col == V:
            return (0, idx)

def add_points(a: tuple, b: tuple) -> tuple:
    return (a[0] + b[0], a[1] + b[1])

def is_in_range(pt):
    r, c = pt
    return 0 <= r < MAX_R and 0 <= c < MAX_C

def get_next_direction(maze: list, pt: tuple, seen: set, map: dict):
    """
    Find the next direction to travel after hitting a waypoint.
    Args:
        maze (list): The maze (constant)
        pt (tuple): The point at which a junction appears
        seen (set): Set of all previously visited points
        map (dict): Compass of directions of travel

    Returns:
        _type_: Enum Constant indicating direction, or None if we've reached the end
    """
    for direction, delta in map.items():
        _pt = add_points(pt, delta)
        if _pt not in seen and is_in_range(pt):
            neighbour = maze[_pt[0]][_pt[1]]
            if neighbour in [V, H] or neighbour in L:
                return direction
    return None

def traverse(maze: list) -> str:
    map = {
        Directions.LEFT:  (0, -1),
        Directions.RIGHT: (0, 1),
        Directions.UP:    (-1, 0),
        Directions.DOWN:  (1, 0)
    }
    
    move_direction = Directions.DOWN
    pt: tuple = find_entry_point(maze[0])
    
    path = []
    stack = [pt]
    seen = set()
    count = 0
    
    while stack:
        curr = stack.pop()
        r, c = curr
        token = maze[r][c]
        
        if token in L:
            path.append(token)
            
        if token == J:
            move_direction = get_next_direction(maze, curr, seen, map)
        
        if move_direction in map.keys() and token != B:
            count += 1
            next_pt = add_points(curr, map[move_direction])
            stack.append(next_pt)

        seen.add(curr)
    return (''.join(path), count)

result1, result2 = traverse(maze)
print(f'Day 19 Part 1: The letters we see after following the routing diagram are {result1}.\n')
print(f'Day 19 Part 2: The packet went exactly {result2} steps.\n')