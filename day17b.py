step_size = 366
max_iterations = 50000000
current_position = 0
value_after_0 = None

for val in range(1, max_iterations + 1):
    current_position = (current_position + step_size) % val + 1
    if current_position == 1:
        value_after_0 = val

result = value_after_0
print(f'Day 17 Part 2: The value after 0 in my completed cirular buffer is {result}.\n')