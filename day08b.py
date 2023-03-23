registers = {}
largest_value = -float('inf')

def modify(val, delta, op):
    ops = {'inc': val + delta, 'dec': val - delta}
    return ops[op]

def compare(val1, val2, comp):
    comparisons = {
        '>': val1 > val2,
        '>=': val1 >= val2,
        '<': val1 < val2,
        '<=': val1 <= val2,
        '!=': val1 != val2,
        '==': val1 == val2
    }
    return comparisons[comp]

with open('inputs/day08.txt', 'r') as file:
    for line in file.readlines():
        sp = line.split()
        reg1, op, val1, _, reg2, comp, val2 = sp
        
        a, b = registers.get(reg1, 0), registers.get(reg2, 0)
        registers[reg1] = modify(a, int(val1), op) if compare(b, int(val2), comp) else a
        if a != b:
            registers[reg2] = b
        largest_value = max(largest_value, registers[reg1])

result = largest_value
print(f'Day 8 Part 2: The largest value ever in any register is throughout execution is {result}.\n')    