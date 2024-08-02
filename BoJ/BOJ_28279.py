import sys
from collections import deque
input = sys.stdin.readline

q = deque()


def solve():
    if command[0] == '1':
        q.appendleft(command[1])

    elif command[0] == '2':
        q.append(command[1])

    elif command[0] == '3':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == '4':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif command[0] == '5':
        print(len(q))
    elif command[0] == '6':
        if not q:
            print(1)
        else:
            print(0)
    elif command[0] == '7':
        if q:
            print(q[0])
        else: 
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)


n = int(input())

for i in range(n):
    command = input().strip().split()
    solve()