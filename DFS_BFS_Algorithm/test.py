import sys
from collections import deque
n, m = map(int, input().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
distance [[-1]*m for _ in range(n)]


q = deque()
# 상하좌우 방향키
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 위치 정보 
for x in range(n):
    for y in range(m):
        if graph[x][y] == 'G':
            q.append((x,y))
            distance[x][y] == 1
        if graph[x][y] == 'N':
            q.appendleft((x,y))
            distance[x][y] == 0
            

# 유령과 마주치게 되는 경우
# 출구에 도착하는 순간 유령과 마주치게 되는 경우

while q:
    x,y = q.popleft()
    if graph[x][y] == 'D':
        print(Yes)
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 미로 밖이면 무시
        if nx < 0 or nx >=n or ny<0 or ny >= m:
            continue
        # 사람인데 다음이 ghost or 벽이면 무시
        if graph[x][y]=='N' and (distance[nx][ny]== 1 or graph[nx][ny]=='#'):
            continue
        if graph[x][y] 
        # ghost인데 다음칸이 ghost이면 무시
        if graph[x][y]=='G' and distance[nx][ny]==1:
            continue
        
        
        
    
    

