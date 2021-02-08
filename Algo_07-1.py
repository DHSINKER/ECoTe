# 07 럭키 스트레이트 1회차
string = input()
length = len(string)
n = int(string)
right, left = 0, 0

for _ in range(length//2):
    right += n%10
    n //= 10

for _ in range(length//2):
    left += n%10
    n //= 10

if right == left:
    print('LUCKY')
else:
    print('READY')
