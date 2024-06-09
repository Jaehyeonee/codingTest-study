# 미로는 최단거리를 찾는 문제로 가장 가까운 노드부터 탐색하는 BFS알고리즘이 사용된다
# BFS : FIFO, queue

from collections import deque
import sys

n, m = map(int, input().split())
graph=[]

graph = [list(map(int, input())) for i in range(n)]
# for i in range(n):
#     graph.append(list(map(int,input())))
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# x,y는 현재위치 1,1
def bfs(x, y):
    q= deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x+dx[i]
            cy = y+dy[i]
            # out bound cas
            if cx < 0 or cy <0 or cx>=n or cy>=m:
                continue
            # wall case
            if graph[cx][cy]==0:
                continue
            if graph[cx][cy]==1:
                graph[cx][cy] = graph[x][y]+1
                q.append((cx,cy))
            print("그래프: ", graph)
            print("큐: ", q)
            
    
    return graph[n-1][m-1]

print(bfs(0,0))








