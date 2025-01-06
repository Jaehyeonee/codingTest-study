import sys
input = sys.stdin.readline

n = int(input())
wire = [tuple(map(int,input().split())) for _ in range(n)]

# print(wire)

# wire.sort( )
# print(wire)
wire.sort()
dp = [1]*n
for i in range(1, n):
    for j in range(0, i)