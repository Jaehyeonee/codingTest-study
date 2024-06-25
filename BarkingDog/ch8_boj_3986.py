"""
    https://www.acmicpc.net/problem/3986
"""

import sys
input = sys.stdin.readline

count =0
n= int(input())

for _ in range(n):
    w = str(input().rstrip())
    stack =[]
    for i in w:
        if not stack:  # 리스트가 비어있으면
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)
    if not stack:
        count += 1

print(count)


