# 19 연산자 끼워 넣기 1회차
from itertools import permutations
n = int(input())
num = list(map(int, input().split()))
temp = list(map(int, input().split()))
oper = []
for i in range(4):
    for j in range(temp[i]):
        oper.append(i)
# 0 plus 1 minus 2 multi 3 divide 
max_result = -1e9
min_result = 1e9

for case in permutations(oper, n-1):
    result = num[0]
    for i in range(n-1):
        if case[i] == 0:
            result += num[i+1]
        elif case[i] == 1:
            result -= num[i+1]
        elif case[i] == 2:
            result *= num[i+1]
        else:
            if result>=0:
                result //= num[i+1]
            else:
                result = -((-result)//num[i+1])
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
