# 08 문자열 재정렬 1회차
string = input()

sum = 0
ch = []

for i in string:
    n = ord(i)
    if n>64:
        ch.append(n)
    else:
        sum += int(i)

ch.sort()

for i in ch:
    print(chr(i), end='')
if sum != 0:    
    print(sum)
