# 15 특정 거리의 도시 찾기 1회차
from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

degree = [1e9]*(n+1)
visited = [False]*(n+1)

queue = deque()
degree[x] = 0
visited[x] = True

for next in graph[x]:
    queue.append((next, 1))

while queue:
    cur, length = queue.popleft()
    degree[cur] = min(length, degree[cur])
    visited[cur] = True
    for next in graph[cur]:
        if not visited[next]:
            queue.append((next, length+1))

if k not in degree:
    print(-1)
else:
    for i in range(n+1):
        if degree[i] == k:
            print(i)
