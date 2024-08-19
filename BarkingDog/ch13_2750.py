import sys
input = sys.stdin.readline

n = int(input())

num = list(int(input()) for _ in range(n))
num.sort()

print(num)
for i in range(n):
    print(num[i])
