# 방탈출 다른 솔루션으로 연습하기 
# 기존 내 아이디어인데, combination으로 모든 조합을 보지 않고
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    visited = [[-1]* M for _ in range(N)]
    q = deque()
    q.append((sx, sy, 1))
    visited[sx][sy] = 1
    max_dist = 0
    max_sum = 0
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1 and graph[nx][ny] !=0 :
                visited[nx][ny] = 1
                q.append((nx, ny, dist+1))

                if dist + 1 > max_dist:
                    max_dist = dist + 1
                    max_sum = graph[nx][ny] + graph[sx][sy]
                elif dist + 1 == max_dist:
                    max_sum = max(max_sum, graph[nx][ny] + graph[sx][sy])

    return max_sum, max_dist


answer = 0
tmp_dist = 0
room = []
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            room.append((i, j))

for sx, sy in room:
    sum_, dist_ = bfs(sx, sy)

    if dist_ > tmp_dist :
        tmp_dist = dist_
        answer = sum_

    elif dist_ == tmp_dist:
        answer = max(answer, sum_)
print(answer)