# 방탈출 : 2023년 LG CNS 3월 ERP직군 3번 유형
from itertools import combinations
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# coord = []
# answer = -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# count = 0
answer = []
def bfs(sx, sy):
    q = deque()
    q.append((sx,sy, 0))
    visited = [[-1]*M for _ in range(N)]
    visited[sx][sy] = 1
    while q:
        x, y , dist = q.popleft()
        flag = False
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny]!=0 and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                q.append((nx, ny, dist+1))
                flag = True
        if not flag:
            answer.append((dist, graph[sx][sy]+ graph[x][y]))


for i in range(N):
    for j in range(M):
        if graph[i][j] > 0:
            bfs(i, j)
            
answer.sort(key=lambda x:(x[0], x[1]), reverse = True)
print(answer[0][1])



# def bfs(sx, sy, ex, ey):
#     q = deque()
#     visited = [[-1]* M for _ in range(N)]
#     global result
#     q.append((sx, sy, 1))
#     visited[sx][sy] = 1
#     while q:
#         x, y, cnt = q.popleft()
#         for d in range(4):
#             nx = x+dx[d]
#             ny = y+dy[d]

#             if (nx, ny) == (ex, ey):
#                 result = graph[sx][sy] + graph[ex][ey]
#                 return result, cnt

#             if(0 <= nx < N and 0 <= ny < M) and (graph[nx][ny] != 0) and (visited[nx][ny] == -1) :
#                 visited[nx][ny] = 1
#                 q.append((nx, ny, cnt+1))
#     return 0, 0

# for i in range(N):
#     for j in range(M):
#         if graph[i][j] != 0 :
#             coord.append([i,j])

# comb = list(combinations(coord, 2))

# for (sx, sy), (ex, ey) in comb:
#     result, dist = bfs(sx, sy, ex, ey)
#     if dist > count:
#         count = dist
#         answer = result
#     elif dist == count:
#         answer = max(answer, result)

#     if dist == 0 and result == 0:
#         answer = 0

# print(answer)