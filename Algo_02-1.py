# 02 곱하기 혹은 더하기 1회차
string = input()

result = 0

for iter in string:
    if result == 0 or iter == '0':
        result += int(iter)
    else:
        result *= int(iter)

print(result)
