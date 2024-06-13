import sys
input = sys.stdin.readline

n = int(input())
stack = []

def push(x):
    stack.append(x)
    return stack

def pop():
    if stack:
        print(stack.pop(0))
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def front():
    if stack:
        print(stack[0])
    else:
        print(-1)

def back():
    if stack:
        print(stack[-1])
    else:
        print(-1)


for i in range(n):
    command = list(input().split())
    if command[0] == 'push':
        x = command[1]
        push(x)
    elif command[0] =="pop":
        pop()
    elif command[0] =="size":
        size()
    elif command[0] =="empty":
        empty()
    elif command[0] =="front":
        front()
    elif command[0] =="back":
        back()