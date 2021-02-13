# 21 인구 이동 1회차
n, l, r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
day = 0
union = [[] for _ in range(n*n)]
visited = [[False]*n for _ in range(n)]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def is_union(y, x, ny, nx):
    if l<=abs(A[y][x]-A[ny][nx])<=r:
        return True
    return False

def search(count, y, x):
    is_uni = False
    for k in move:
        ny = y+k[0]
        nx = x+k[1]
        if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and is_union(y, x, ny, nx):
            is_uni = True
            visited[ny][nx] = True
            union[count].append((ny, nx))
            search(count, ny, nx)
    return is_uni
    

while True:
    union = [[] for _ in range(n*n)]
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if search(count, i, j):
                    union[count].append((i, j))
                    count += 1
    if count == 0:
        break
    
    for i in range(count):
        sum = 0
        for pos in union[i]:
            sum += A[pos[0]][pos[1]]
        sum //= len(union[i])
        for pos in union[i]:
            A[pos[0]][pos[1]] = sum
        
    day += 1

print(day)
