from functools import reduce

def to_hex_string(raw_values: list) -> str:
    hex_string = ''
    for i in range(0, 256, 16):
        # XOR each element in each group of 16 elements together to produce a result
        # Add the hex string version of that result to the final return value
        hex_string += str(hex(reduce(lambda a, b: a ^ b, raw_values[i : i + 16])))[2:]
    
    return hex_string

def generate_hash(input: str):
    pos = 0
    skip_size = 0

    # ASCII codes for the input string, plus the suffix
    ascii_values  = [ord(n) for n in input] + [17, 31, 73, 47, 23]

    # Range from 0-255, which will be rearranged according to the set of ASCII values
    hashed_values = [i for i in range(256)]

    for _ in range(64):

        for length in ascii_values:
            # Add the current ASCII value representing a length to the current position to find the target distance
            dist = pos + length

            if dist >= 256:
                # Need to wrap around the list and reverse from `pos` to the end of the list,
                # to the start of the list + `dist` % 256 (the amount of hashed values)
                dist %= 256
                sub_list = list(reversed(hashed_values[pos:] + hashed_values[:dist]))
                hashed_values = sub_list[length - dist:] + hashed_values[dist:pos] + sub_list[:length - dist]
            else:
                # No need to wrap around, just reverse the range from `pos` to `dist`
                sub_list = list(reversed(hashed_values[pos:dist]))
                hashed_values = hashed_values[:pos] + sub_list + hashed_values[dist:]
            
            pos = (pos + length + skip_size) % 256
            skip_size += 1

    # This will return a list of numbers from 0-255 in some order
    return hashed_values

with open('inputs/day10.txt', 'r') as file:
    hashed_values = generate_hash(file.readline())
    result = to_hex_string(hashed_values)

if __name__ == '__main__':
    # Day 14 uses this as well
    print(f'Day 10 Part 2: The knot hash of the puzzle input is {result}.\n')    