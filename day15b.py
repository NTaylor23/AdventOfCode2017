def a_generator():
    n = 289
    while True:
        n *= 16807
        n %= 2147483647
        if n % 4 == 0:
            yield n & 0xFFFF

def b_generator():
    n = 629
    while True:
        n *= 48271
        n %= 2147483647
        if n % 8 == 0:
            yield n & 0xFFFF

def calculate():
    A = a_generator()
    B = b_generator()

    count = 0

    for _ in range(5000000):
        a = next(A)
        b = next(B)
        if a == b:
            count += 1

    return count

result = calculate()
print(f'Day 15 Part 2: After 5 million pairs, using this new generator logic, the judge\'s final count is {result}.\n')
