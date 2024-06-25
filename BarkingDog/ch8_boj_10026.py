import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(input().strip()) for _ in range(n)]
q= deque()
visited = [[0]*n for _ in range(n)]
# 상하좌우 00 01 02 03 04
#        10 11 12 13 14
dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

answer1 = 0
answer2 = 0

def bfs(x,y):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and maps[x][y]==maps[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] =1
                q.append((nx,ny)) 

# 적록색약이 아닌 경우    
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            answer1 +=1

# 적록색약인경우
for i in range(n):
    for j in range(n):
        if maps[i][j]=="R":
            maps[i][j] = "G"

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            answer2+=1

print(answer1, answer2)