# 12 기둥과 보 설치 1회차x
def is_gi(current, x, y):
    if y == 0:  # 바닥 위인 경우
        return True
    
    if current[y-1][x]%2 == 1:  # 기둥 위인 경우
        return True

    if current[y][x-1]>1 or current[y][x]>1:    # 보의 한쪽 끝부분 위인 경우
        return True
    return False

def is_bo(current, x, y):
    if current[y][x-1]>1 and current[y][x+1]>1: # 양쪽 끝부분이 보와 연결된 경우
        return True
    
    if current[y-1][x]%2 == 1 or current[y-1][x+1]%2 == 1:  # 한쪽 끝부분이 기둥 위인 경우
        return True
    return False

# 기둥 1 보 2 둘 다 존재 3
def solution(n, build_frame):
    answer = []
    m = [[0]*(n+1) for _ in range(n+1)]
    for frame in build_frame:
        x, y, a, b = frame
        if a == 0:
            if b == 0:
                m[y][x] -= 1
                if is_gi(m, x, y+1) and is_bo(m, x-1, y+1) and is_bo(m, x, y+1):
                    answer.remove((x, y, a))
                else: m[y][x] += 1
            else:
                if is_gi(m, x, y):
                    answer.append((x, y, a))
                    m[y][x] += 1
        else:
            if b == 0:
                m[y][x] -= 2
                if is_gi(m, x, y) and is_gi(m, x+1, y) and is_bo(m, x-1, y) and is_bo(m, x+1, y):
                    answer.remove((x, y, a))
                else: m[y][x] += 2
            else:
                if is_bo(m, x, y):
                    answer.append((x, y, a))
                    m[y][x] += 2
    print(answer)
    answer = sorted(answer, key= lambda k: (k[0]*100+k[1]*10+k[2]))
    print(answer)
    return answer
