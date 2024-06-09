

# https://softeer.ai/practice/7726

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph=[]
q = deque()
exitloc =[]
namwoo =[]
ghost = deque()


# 격자 정보
for i in range(n):
    li = list(sys.stdin.readline())

    if 'N' in li: # 남우 좌표 저장
        x, y = i, li.index('N')
        namwoo.append((x,y))
        q.append((x,y))
    if 'G' in li: # ghost 좌표 저장
        x, y = i, li.index('G')
        ghost.append((x,y))
    if 'D' in li: # 탈출구 좌표 저장
        x, y = i, li.index('D')
        exitloc.append(x)
        exitloc.append(y)

    graph.append(li)
print(q)
print(namwoo)

# 맨해튼 거리로 출구과 남우 위치의 최소 거리
initial_dist = 0
initial_dist = abs(namwoo[0][0]-exitloc[0]) + abs(namwoo[0][1]-exitloc[1])

ghost_short = int(1e9)

while ghost:
    x,y = ghost.popleft()
    ghost_short = min(ghost_short, abs(x-exitloc[0])+abs(y-exitloc[1]))

# 유령이 먼저 도착하니까 남우가 탈출할 수 없음.    
if ghost_short <= initial_dist:
    print("No")

else:
    visit = [[0]* m for _ in range(n)]
    dx = [-1, 1, 0 ,0]
    dy = [0 ,0 , -1, 1]

    exit_time = int(1e9)

    while q:
        print("q: ", q)
        print(visit)
        x, y = q.popleft()

        for i in range(4): # 상하좌우 4개 방향 돌기
            nx = x+dx[i]
            ny = y+dy[i]

            print("현좌표: ", (nx,ny))

            # 진행가능한 방향이라면
            if 0<= nx < n and 0<= ny < m and (graph[nx][ny]=='.' or graph[nx][ny]=='D'):
                q.append((nx,ny))
                visit[nx][ny] = 1

            elif visit[nx][ny] == 1:
                continue
        
        


        if graph[x][y] == 'D':
            print("도착")
            break
        


            

        