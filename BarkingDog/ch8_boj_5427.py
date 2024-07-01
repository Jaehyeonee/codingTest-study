import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()


def bfs():
    while q:
        # print(q)
        x, y = q.popleft()
        # print(x,y)
        cur = graph[x][y] # 현재위치
        # print("현재위치", cur)
        for i in range(4):
            nx, ny =x+dx[i], y+dy[i]
            
            if cur == '*':
                if ny <= 0 or ny >w-1 or nx <= 0 or nx >h-1:
                    continue
            # 이미 방문한 곳이면 무시
            if visited[nx][ny] != -1:
                continue
            if graph[nx][ny] == '*':
                continue
            if graph[nx][ny] == '#':
                continue
            # if graph[nx][ny] == '@':
            #     continue
            if cur == '@':
                # print("얘는 상근이",cur)
                if ny < 0 or ny >w-1 or nx < 0 or nx >h-1 :
                    print("count: ",visited[nx][ny] + 1)
                    break
                if graph[nx][ny] == '.': 
                    visited[nx][ny] = visited[x][y] + 1    
                    print(visited)
            graph[nx][ny] = cur # 다음좌표를 상근이 or 물로 변경
            q.append((nx,ny))
        else:
            
            continue
        break
    else:
        print("IMPOSSIBLE")

n = int(input())
for i in range(n):
    w, h = map(int, input().split())
    visited = [[-1]*w for _ in range(h)]
    graph = [list(input().strip()) for _ in range(h)]
    for x in range(h):
        for y in range(w):
            if graph[x][y] == '*':
                q.appendleft((x,y))
            elif graph[x][y] =='@':
                q.append((x,y))
                visited[x][y] = 0
            
                
    bfs()
            
