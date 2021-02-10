# 13 치킨 배달 1회차
from itertools import combinations
n, m = map(int, input().split())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

home = []
chick = []
result = 0
for i in range(n):
    for j in range(n):
        if info[i][j] == 1:
            home.append([i, j])
        elif info[i][j] == 2:
            chick.append([i, j])
    

def chick_len(h, c):
    sum = 0
    for i in h:
        m = 1e9
        for j in c:
            m = min(abs(i[0]-j[0])+abs(i[1]-j[1]), m)
        sum += m
    return sum

chick_combi = list(combinations(chick, m))

result = 1e9

for c in chick_combi:
    result = min(chick_len(home, c), result)

print(result)
