# 05 볼링공 고르기 1회차
n, m = map(int, input().split())
balls = list(map(int, input().split()))

result = 0

for i in range(n-1):
    for ball in balls[i+1:]:
        if balls[i] != ball:
            result += 1

print(result)
