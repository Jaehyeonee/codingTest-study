from collections import deque
import sys

N = int(sys.stdin.readline())

deq = deque()

def empty():
    if len(deq) == 0:
        return 1
    else:
        return 0

def size():
    return len(deq)


for i in range(N):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push_front':
        deq.appendleft(cmd[1])

    elif cmd[0] == 'push_back':
        deq.append(cmd[1])

    elif cmd[0] == 'pop_front':
        if empty()==1:
            print("-1")

        else:
            tmp = deq.popleft()
            print(tmp)

    elif cmd[0] == 'pop_back':
        if empty() == 1:
            print("-1")
        else:
            tmp = deq.pop()
            printf(tmp)

    elif cmd[0] == 'front':
        if empty()==1:
            print("-1")
        else:
            printf(deq[0])

    elif cmd[0] == 'back':
        if empty() == 1:
            print("-1")

        else:
            print(deq[len(deq)-1])

    elif cmd[0] == 'size':
        printf(size())

    elif cmd[0] == 'empty':
        print(empty())
