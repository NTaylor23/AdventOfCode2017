from day10b import generate_hash, to_hex_string

INPUT = 'ffayrhll'
GRID_SIZE = 128
DELTAS = [1, -1, 1j, -1j]

grid = []

def append_binary_array(hex_string: str) -> None:
    bit_length = 4
    row = []
    for char in hex_string:
        bytes_array = [int(n) for n in list(bin(int(char, 16))[2:].zfill(bit_length))]
        row.extend(bytes_array)
    return row
    
result = 0

for i in range(GRID_SIZE):
    word = INPUT + f'-{i}'
    hash = generate_hash(word)
    hex_string = to_hex_string(hash)
    row = append_binary_array(hex_string)
    grid.append(row)

def count_islands(grid) -> int:
    neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)] # Right, Up, Down, Left
    seen = set()

    def dfs(pos: tuple, num: int):
        stack = [pos]
        while stack:
            y, x = stack.pop()
            grid[y][x] = num
            seen.add((y, x))
            for dy, dx in neighbors:
                _y, _x = y + dy, x + dx

                is_in_bounds = 0 <= _y < GRID_SIZE and 0 <= _x < GRID_SIZE
                is_unseen = (_y, _x) not in seen

                if is_in_bounds and is_unseen:
                    if grid[_y][_x] == 1:
                        stack.append((_y, _x))
        
    count = 0

    for i, row in enumerate(grid):
        for j, bit in enumerate(row):
            pos = (i, j)
            if bit == 1 and pos not in seen:
                count += 1
                dfs(pos, count)    

    return count

result = count_islands(grid)
print(f'Day 14 Part 2: The number of islands in the grid is {result}.\n')
