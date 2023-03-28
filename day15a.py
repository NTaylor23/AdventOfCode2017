from cython_files import day15a_cy

result = day15a_cy.calculate(289, 629, 16807, 48271)
print(f'Day 14 Part 1: After 40 million pairs, the judge\'s final count is {result}.\n')
