## 토마토 문제
import sys
from collections import deque
input = sys.stdin.readline
# 가로, 세로, 높이
m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q= deque()
# 상하좌우 위 아래
dx=[-1, 1, 0, 0, 0, 0]
dy=[0, 0, -1, 1, 0, 0]
dz=[0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]

            if 0<= nx < n and 0<=ny<m and 0<=nz<h:
                if tomato[nz][nx][ny] == 0 : # 익지 않은 토마토이면
                    tomato[nz][nx][ny] = tomato[z][x][y] +1
                    q.append((nz,nx,ny))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))

bfs()
count = 0
flag = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                flag = True

            count = max(count, tomato[i][j][k] )


if flag :
    print(-1)
else:
    print(count -1)