import sys
input = sys.stdin.readline

n = int(input())
point = []

for _ in range(n):
    x, y = map(int,input().split())
    point.append((x,y))

point.sort(key = lambda x: (x[1], x[0]))
for i in range(n):
    print(' '.join(map(str, point[i])))