import heapq
n = int(input())
ho = list(map(int, input().split()))
ho.sort()
group = 0

while ho:
    count = 0
    maxh = heapq.heappop(ho)
    count+=1
    if maxh == count:
        group += 1
        continue
    while ho:
        now = heapq.heappop(ho)
        count+=1
        if now>maxh:
            maxh = now
        if maxh == count:
            group+=1
            break

print(group)
