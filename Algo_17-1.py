# 17 경쟁적 전염 1회차
from collections import deque
n, k = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

queue = deque()

for i in range(n):
    for j in range(n):
        if lab[i][j] != 0:
            queue.append((0, lab[i][j], i, j))

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while queue:
    time, vi, cy, cx = queue.popleft()
    if time == s:
        break
    for i in range(4):
        ny = cy + move[i][0]
        nx = cx + move[i][1]
        if 0<=ny<n and 0<=nx<n and lab[ny][nx] == 0:
            lab[ny][nx] = vi
            queue.append((time+1, vi, ny, nx))

print(lab[x-1][y-1])
