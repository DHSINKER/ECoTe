# 03 문자열 뒤집기 1회차
string = input()
current = string[0]
n = 1
for s in string[1:]:
    if current != s:
        current = s
        n += 1
print(n//2)
