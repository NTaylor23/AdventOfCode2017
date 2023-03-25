from functools import reduce

SIZE = 256
pos = 0
skip_size = 0
suffix = [17, 31, 73, 47, 23]

string = [i for i in range(SIZE)]

with open('inputs/day10.txt', 'r') as file:
    lengths = [ord(n) for n in file.readline()] + suffix

for _ in range(64):
    for length in lengths:
        dist = pos + length
        if dist >= SIZE:
            dist %= SIZE
            sub_list = list(reversed(string[pos:] + string[:dist]))
            string = sub_list[length - dist:] + string[dist:pos] + sub_list[:length - dist]
        else:
            sub_list = list(reversed(string[pos:dist]))
            string = string[:pos] + sub_list + string[dist:]
        pos = (pos + length + skip_size) % SIZE
        skip_size += 1

hex_string = ''
for i in range(0, SIZE, 16):
    hex_string += str(hex(reduce(lambda a, b: a ^ b, string[i : i + 16])))[2:]
    
result = hex_string
print(f'Day 10 Part 2: The knot hash of the puzzle input is {result}.\n')    
