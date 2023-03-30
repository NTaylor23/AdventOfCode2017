from cython_files import day15a_cy
# 40 million iterations? In Python? I don't C why not...

"""
def calculate(long a, long b, int a_factor, int b_factor):
    cdef int divisor, mask, count
    divisor = 2**31 - 1
    mask = 0xFFFF
    count = 0
    for _ in range(40000000):
        a = (a * a_factor) % divisor
        b = (b * b_factor) % divisor
        count += (a & mask == b & mask)
    return count
"""

result = day15a_cy.calculate(289, 629, 16807, 48271)
print(f'Day 15 Part 1: After 40 million pairs, the judge\'s final count is {result}.\n')
