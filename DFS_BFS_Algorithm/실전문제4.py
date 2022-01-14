#https://sigcho.tistory.com/117

# DFS,BFS 4. ** 상하좌우, 그래프 형태의 모델링, 방문처리 등

# bfs : 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다
#상하좌우로 연결되는 모든 노드로의 거리가 1로 동일하다
#따라서 BFS를 수행하면 '모든 노드의 최단거리 값을 기록'하여 해결할 수 있다.


# DFS: 1. 특정한 지점의 주변 상하좌우를 살핀후, 주변지점 중에서 값이 0 이면서 아직 방문하지 않은 지점이 있다면 방문.
# 2. 방문한 지점에서 다시 상하좌우를 사려 방문 진행 과정을 반복하면, 연결된 모든 지점을 방문할 수 있다.
# 3. 모든 노드에 대하여 반복하며, 방문하지 않은 지점의 수를 카운트 한다. 


from collections import deque

n, m = map(int,input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maze_map=[]

for _ in range(n):
    maze_map.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # (x,y)인 튜플데이터를 담는다.

    while queue: #queue가 빌 때 까지
        x, y = queue.popleft() #반복 할 때마다 큐에서 원소를 꺼냄
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]

            if nx >=0 and ny >=0 and nx <n and ny<m:
                if maze_map[nx][ny] ==1:
                    maze_map[nx][ny]= maze_map[x][y] +1
                    queue.append((nx,ny))
                
            

    return maze_map[n-1][m-1] # 가장 오른쪽 아래까지의 최단거리 반환


                
print(bfs(0, 0))
