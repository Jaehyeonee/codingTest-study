import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs():
    while q:
        
        x, y = q.popleft()
       
        cur = graph[x][y] # 현재위치
        for i in range(4):
            nx, ny =x+dx[i], y+dy[i]
            if cur == '*':
                if ny < 0 or ny >= w or nx < 0 or nx >= h:
                    continue
            # elif cur == '@':
            else:
                if ny < 0 or ny >= w or nx < 0 or nx >= h:
                    
                    return visited[x][y] + 1
                    # break    #>> 여기에 break를 하게 되면 while문을 빠져나가서 else를 만나 항상 IMPOSSIBLE 출력
                    
                visited[nx][ny] = visited[x][y] + 1
                
            
            if graph[nx][ny] == '*':
                continue
            if graph[nx][ny] == '#':
                continue
            
        
            
            if graph[nx][ny] == '@':
                continue;
            
            graph[nx][ny] = cur # 다음좌표를 상근이 or 물로변경
            q.append((nx,ny))
    return "IMPOSSIBLE"
    
    


n = int(input())
for i in range(n):
    w, h = map(int, input().split())

    q = deque()
    visited = [[-1]*w for _ in range(h)]
    graph = [list(input().strip()) for _ in range(h)]
    for x in range(h):
        for y in range(w):
            if graph[x][y] == '*':
                q.appendleft((x,y))
            elif graph[x][y] =='@':
                q.append((x,y))
                visited[x][y] =0
                
    print(bfs())
            
