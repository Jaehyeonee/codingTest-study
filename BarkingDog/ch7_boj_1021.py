import sys
from collections import deque
input = sys.stdin.readline
q = deque()

def f_pop():
    q.popleft()
    return q

def l_move():
    q.append(q.popleft())
    return q

def r_move():
    q.appendleft(q.pop())
    return q

n = int(input())

for i in range(1,n+1):
    q.append(i)
