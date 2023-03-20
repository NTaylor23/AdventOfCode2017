with open('inputs/day01.txt', 'r') as file:
    captcha = file.readline()

result = sum(int(a) for (a, b) in zip(captcha[-1] + captcha[:-1], captcha) if a == b)
print(f'Day 1 Part 1: The solution to my Captcha is {result}.\n')