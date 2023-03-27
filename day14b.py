from day10b import generate_hash, to_hex_string

INPUT = 'ffayrhll'
GRID_SIZE = 128
DELTAS = [1, -1, 1j, -1j]

grid = []

def append_binary_array(hex_string: str) -> None:
    bit_length = 4
    row = []
    for char in hex_string:
        row.extend([int(n) for n in list(bin(int(char, 16))[2:].zfill(bit_length))])
    return row
    
result = 0

for i in range(GRID_SIZE):
    word = INPUT + f'-{i}'
    hash = generate_hash(word)
    hex_string = to_hex_string(hash)
    row = append_binary_array(hex_string)
    grid.append(row)

seen = set()

def dfs(idx, pos, seen, grid):
    y, x  = pos
    stack = [(y, x)]
    while stack:
        pass

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        pass