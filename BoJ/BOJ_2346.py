import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
numbers = deque(list(map(int, input().strip().split())))
idx = deque([i for i in range(1,n+1)])
ballon = []

while numbers:
    num = numbers.popleft()
    ballon.append(idx.popleft())

    if num > 0:
        numbers.rotate(-(num-1))
        idx.rotate(-(num - 1))
    else:
        numbers.rotate(-num)
        


