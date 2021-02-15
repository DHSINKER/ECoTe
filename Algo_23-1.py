# 23 국영수 1회차
import sys
n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
    name, ko, math, en = sys.stdin.readline().rstrip().split()
    data.append((name, int(ko), int(math), int(en)))

# 국어 내림 영어 오름 수학 내림 이름 오름
data.sort(key =lambda x: (-x[1], x[2], -x[3], x[0]))

for i in data:
    print(i[0])
