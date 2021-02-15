# 24 안테나 1회차
import sys
n = int(sys.stdin.readline().rstrip())
data = []
for i in list(sys.stdin.readline().rstrip()):
    if i != ' ':
        data.append(int(i))
#data = list(map(int, input().split()))
min_value = 1e9
result = 0
for i in data:
    sum = 0
    for j in data:
        sum+=abs(i-j)
    if min_value > sum:
        min_value = sum
        result = i
print(result)
