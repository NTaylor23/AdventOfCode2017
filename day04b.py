with open('inputs/day04.txt', 'r') as file:
    passphrases = [phrase.strip().split() for phrase in file.readlines()]

result = 0
for line in passphrases:
    # Sort each word lexicographically, check if any two words are the same (i.e. anagrams)
    result += int(len(set([''.join(sorted(s)) for s in line])) == len(line))
print(f'Day 4 Part 2: {result} passphrases contain no anagrams.\n')