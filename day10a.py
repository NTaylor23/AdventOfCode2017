SIZE = 256
pos = 0
skip_size = 0

string = [i for i in range(SIZE)]

with open('inputs/day10.txt', 'r') as file:
    lengths = [int(n.strip()) for n in file.readline().split(',')]

for length in lengths:
    if length > SIZE:
        continue

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

result = string[0] * string[1]
print(f'Day 10 Part 1: The result of multiplying the first two numbers in the list is {result}.\n')    