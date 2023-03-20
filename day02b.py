with open('inputs/day02.txt', 'r') as file:
    spreadsheet = [[int(a) for a in row.strip().split()] for row in file.readlines()]

def find_divisible_numbers(row: list) -> int:
    """Find the two numbers in `row` which are evenly divisible with each other.
    E.G. in [5, 9, 2, 8], return 8 / 2.

    Args:
        row (list): a list of numbers such that exactly two are divisible with each other.

    Returns:
        int: the quotient of the two divisible numbers.
    """
    n = len(row)
    for i in range(n):
        for j in range(i + 1, n):
            if row[i] % row[j] == 0:
                return row[i] // row[j]
            elif row[j] % row[i] == 0:
                return row[j] // row[i]
    return 0

result = sum(find_divisible_numbers(row) for row in spreadsheet)
print(f'Day 2 Part 2: The sum of each row\'s result is {result}.\n')
