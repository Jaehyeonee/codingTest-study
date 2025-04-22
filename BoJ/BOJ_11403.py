import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# DFS
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*n for _ in range(n)]
coord = defaultdict(list)
for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            coord[i].append(j)

def dfs(start,v, visited):
    for nxt in coord[v]:
        if visited[nxt]== 0:
            visited[nxt] = 1
            answer[start][nxt] = 1
            dfs(start, nxt, visited)


for i in range(n):
    visited = [0]*n
    dfs(i,i,visited)

for row in answer:
    print(*row)