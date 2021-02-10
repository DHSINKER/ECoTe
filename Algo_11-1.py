# 11 뱀 1회차
from collections import deque
# 보드의 크기, 사과의 개수 입력
n = int(input())
k = int(input())
# 맵 생성 및 사과의 위치 입력
apple = [[0]*n for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    apple[y-1][x-1] += 1
# 뱀의 방향 변환 횟수 및 정보 입력
l = int(input())
queue = deque()
for _ in range(l):
    t, d = input().split()
    queue.append((int(t), d))
# 방향 정보
E, S, W, N = 0, 1, 2, 3
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snake_d = E
snake = [[0]*n for _ in range(n)]
snake[0][0] += 1
snake_pos =[[0, 0]]
time = 0

while True:
    if queue and time == queue[0][0]:
        t, d = queue.popleft()
        snake_d = (snake_d+5)%4 if d=='D' else (snake_d+3)%4
    time += 1
    new_head = [snake_pos[0][0]+direction[snake_d][0], snake_pos[0][1]+direction[snake_d][1]]
    if not (0<=new_head[0]<n) or not (0<=new_head[1]<n) or snake[new_head[0]][new_head[1]] == 1:
        break
    snake_pos.insert(0, new_head)
    snake[snake_pos[0][0]][snake_pos[0][1]] += 1
    if apple[snake_pos[0][0]][snake_pos[0][1]] == 1:
        apple[snake_pos[0][0]][snake_pos[0][1]] -= 1
    else:
        snake[snake_pos[-1][0]][snake_pos[-1][1]] -= 1
        snake_pos.pop()
    
print(time)
