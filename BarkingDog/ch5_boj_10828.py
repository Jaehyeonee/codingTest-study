"""
https://www.acmicpc.net/problem/10828
"""

import sys
input = sys.stdin.readline
stack = []

def push(x):
    stack.append(x)
    return stack

def pop():
    if stack:
        print(stack.pop())    
    else:
        print(-1)

def size():
    print(len(stack))

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

def empty():
    if stack:
        print(0)
    else:
        print(1)

n = int(input())

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'top':
        top()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'pop':
        pop()

