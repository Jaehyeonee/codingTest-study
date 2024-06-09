import sys
input = sys.stdin.readline
k = int(input())
stack = []

for i in range(k):
    num = int(input())
    if num == 0 and stack:
        stack.pop()
    else:
        stack.append(num)

res = sum(stack)

print(res)