
'''
Queue에 남우를 먼저 넣고 ghost를 넣어서 진행
'''
# https://softeer.ai/practice/7726

from collections import deque
n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(n)]
# print(graph)
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while len(q) != 0:
        x, y, char = q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            #격자 범위에 있는동안
            if 0 <= nx < n and 0 <= ny < m:
                # 현재 남우일 때
                if char == 'N':
                    # 탈출구이면 answer를 yes로
                    if graph[nx][ny] == 'D':     
                        answer = 'Yes'
                        return answer
                    # 현재 위치에서 이동할 다음 칸이 ghost, 남우 둘다 방문한 적이 없고 빈칸이면      
                    if visted_ghost[nx][ny] == 0 and visited_namu[nx][ny] == 0 and graph[nx][ny] == '.':
                        # 남우가 방문한 것으로 표시
                        visited_namu[nx][ny] = 1
                        # 이동한 새로운 위치를 queue에 넣어줌
                        q.append((nx, ny, char))
                # 현재 ghost일 때
                elif char == 'G':
                    # ghost가 방문한 적 없는 곳이면
                    if visted_ghost[nx][ny] == 0:
                        # 방문 처리하고, 
                        visted_ghost[nx][ny] = 1
                        # 이동한 새로운 ghost위치를 q에 삽입
                        q.append((nx, ny, char))

    # 탈출구를 찾지 못했다면 answer= no
    answer = 'No'
    return answer
                        
                                    
q = deque()
# ghost와 남우의 방문 처리를 따로 해줌.
visted_ghost = [[0] * m for _ in range(n)]
visited_namu = [[0] * m for _ in range(n)]


# extend하기 위한 임시 배열
ghost = []

# 초기에 남우와 귀신이 있는 위치 정보 queue에 담기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'N':
            q.append((i, j, 'N'))
            visited_namu[i][j] = 1    #처음 남우가 있던 곳은 방문한 것으로 해줘야 하니까
        if graph[i][j] == 'G':
            ghost.append((i, j,'G'))
            visted_ghost[i][j] = 1    #처음 ghost들이 있던 곳은 방문한 것으로 해줘야 하니까 (ghost는 1개 이상일 수 있음)
            
q.extend(ghost) # extend 함수로 남우의 큐 뒤에 ghost 정보 추가
print(bfs())

        
