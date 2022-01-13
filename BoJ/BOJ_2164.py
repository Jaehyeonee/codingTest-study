
#백준 2164번 '카드2'

import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()

for i in range(N):
    deq.append(i+1)


while len(deq) > 1:
    print(deq)
    deq.popleft()
    deq.append(deq.popleft())
    

print(deq.pop())
