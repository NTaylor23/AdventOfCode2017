with open('inputs/day01.txt', 'r') as file:
    captcha = file.readline()

n = len(captcha)
halfway = n // 2

result = sum(int(num) for (idx, num) in enumerate(captcha) if num == captcha[(idx + halfway) % n])
print(f'Day 1 Part 2: The solution to my *new* Captcha is {result}.\n')