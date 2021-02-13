# 20 감시 피하기 1회차
n = int(input())
floor = []
for _ in range(n):
    floor.append(list(input().split()))

result = 'NO'

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def check():
    for i in range(n):
        for j in range(n):
            if floor[i][j] == 'S':
                for m in move:
                    y, x = i, j
                    while 0<=y<n and 0<=x<n and floor[y][x] != 'O':
                        if floor[y][x] == 'T':
                            return False
                        y += m[0]
                        x += m[1]
    return True

def dfs(count):
    global result
    if count == 3:
        if check():
            result = 'YES'
        return
    else:
        for i in range(n):
            for j in range(n):
                if floor[i][j] == 'X':
                    floor[i][j] = 'O'
                    dfs(count+1)
                    floor[i][j] = 'X'    

dfs(0)
print(result)
