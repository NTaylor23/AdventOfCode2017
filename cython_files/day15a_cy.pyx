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