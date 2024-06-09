# #https://www.acmicpc.net/problem/3055
import sys
from collections import deque

n, m = map(int, input().split())
graph =[list(sys.stdin.readline().strip()) for _ in range(n)]
distance = [[-1]* m for _ in range(n)]
dx = [-1, 1 ,0 ,0]
dy = [0, 0 , -1, 1]
q = deque()

# def bfs(Dx, Dy):
#     while q:
#         x, y = q.popleft()
#         if graph[Dx][Dy] == 'S':
#             return distance[Dx][Dy]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < m:
#                 if (graph[nx][ny]=='.' or graph[nx][ny]=='D') and graph[x][y]=='S' :
#                     graph[nx][ny] == 'S'
#                     distance[nx][ny] = distance[x][y] + 1
#                     q.append((nx, ny))
#                 elif (graph[nx][ny]=='.' or graph[nx][ny]=='S') and graph[x][y] == '*':
#                     graph[nx][ny] = '*'
#                     q.append((nx, ny))
#                 else:
#                     continue
#     return "KAKTUS"


# for x in range(n):
#     for y in range(m):
#         if graph[x][y] == 'S':
#             q.append((x,y))
#         elif graph[x][y] == 'D':
#             Dx,Dy = x,y

# for x in range(n):
#     for y in range(m):
#         if graph[x][y] == '*':
#             q.append((x,y))


# print(bfs(Dx, Dy))
            
'''
다른 솔루션------- 물을 먼저 증가시키기
'''


for x in range(n):
    for y in range(m):
        if graph[x][y] == 'S':
            q.append((x, y))
            distance[x][y] = 0
        elif graph[x][y] == '*':
            q.appendleft((x,y))
            print(x,y)
            

while q:
    x, y = q.popleft()
    cur = graph[x][y]
    print(graph[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 밖이면 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 방문한 곳이면 무시
        if distance[nx][ny] != -1:
            continue
        # 다음 위치가 물이거나 돌이면 무시
        if graph[nx][ny] == '*' or 'X':
            continue
        # if graph[ny][nx] == "*":  # 물 무시
        #     continue
        # if graph[ny][nx] == "X":  # 돌 무시
        #     continue
    
        # 물이 비버네 들어가려면
        if cur == '*' and graph[nx][ny]=='D':
            continue
        if cur == 'S':
            if graph[nx][ny]=='D':
                print(distance[x][y]+1)
                break
            distance[nx][ny] = distance[x][y] + 1
        
        graph[nx][ny] = graph[x][y]
        q.append((nx,ny))

    else:
        continue
    break
else:
    print("KAKTUS")


    

    