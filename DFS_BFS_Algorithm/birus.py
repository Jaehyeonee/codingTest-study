import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
max_safe = 0


# 미리 바이러스 위치 저장
virus_pos = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]
# 미리 빈 공간 위치 저장
empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

def bfs():
    temp = [row[:] for row in graph]
    q = deque(virus_pos)
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if temp[nx][ny] == 0 :
                    temp[nx][ny] = 2
                    q.append((nx,ny))
    return sum(row.count(0) for row in temp)

def solution(count, start):
    global max_safe
    if count == 3:
        max_safe = max(max_safe, bfs())
        return
    for i in range(start, len(empty)):
        x, y = empty[i]
        graph[x][y] = 1
        solution(count + 1, i + 1)
        graph[x][y] = 0


    # dfs 방식은 바로 시간초과남
    # for i in range(n):
    #     for j in range(m):
    #         if graph[i][j] == 0:
    #             graph[i][j] = 1
    #             solution(count + 1)
    #             graph[i][j] = 0

solution(0,0)
print(max_safe)
