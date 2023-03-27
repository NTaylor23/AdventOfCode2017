from day10b import generate_hash, to_hex_string # Knot Hash realness

INPUT = 'ffayrhll'
GRID_SIZE = 128

def count_set_bits(hex_string: str) -> int:
    bit_length = 4
    sum = 0
    for char in hex_string:
        binary = bin(int(char, 16))[2:].zfill(bit_length)
        sum += binary.count('1')
    return sum

result = 0

for i in range(GRID_SIZE):
    word = INPUT + f'-{i}'
    hash = generate_hash(word)
    hex_string = to_hex_string(hash)
    result += count_set_bits(hex_string)

print(f'Day 14 Part 1: The number of squares used across the 128*128 grid is {result}.\n')
