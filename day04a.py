with open('inputs/day04.txt', 'r') as file:
    passphrases = [phrase.strip().split() for phrase in file.readlines()]

result = 0
for line in passphrases:
    result += int(len(set(line)) == len(line))
print(f'Day 4 Part 1: {result} passphrases contain no duplicated words.\n')