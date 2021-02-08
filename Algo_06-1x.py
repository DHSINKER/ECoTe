# 06 무지의 먹방 라이브 1회차x
import heapq
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    length = len(food_times)
    max = length
    q = []
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    pre = 0
    while (q[0][0]-pre)*length<k:
        time, num = heapq.heappop(q)
        k -= (time-pre)*length
        length -= 1
        pre = time
    q = sorted(q, key =lambda x:x[1])
    return q[(k+1)%(length)-1][1]
