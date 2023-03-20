with open('inputs/day02.txt', 'r') as file:
    spreadsheet = [[int(a) for a in row.strip().split()] for row in file.readlines()]

result = sum(max(row) - min(row) for row in spreadsheet)
print(f'Day 2 Part 1: The checksum for the spreadsheet is {result}.\n')