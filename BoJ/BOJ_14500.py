# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# visited = [[0]*M for _ in range(N)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # leve : 테트로미노 칸수가 4개에 해당하면 끝
# # temp : 칸들의 합을 담음 
# # path : 지금까지 선택된 칸들을 담아서 모든 인접한, 현재 모양의 모든 셀의 이웃을 확장
# def solution(level, path, temp):
#     global ans
#     if level == 4:
#         ans = max(temp, ans)
#         return

#     for x, y in path:
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 :
#                 visited[nx][ny] = 1
#                 solution(level+1, path + [(nx, ny)], temp + graph[nx][ny])
#                 visited[nx][ny] = 0
#     return
# ans = 0

# for i in range(N):
#     for j in range(M):
#         solution(1,[(i, j)], graph[i][j])
# print(ans)
def solution(n):
    answer = [[0] * n for _ in range(n)]
    # 우 하 좌 상
    dx = [0,1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = 0,0
    answer[x][y] = 1
    for i in range(0, (n*n)):
        answer[x][y] = i + 1
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<ny<n and answer[nx][ny] == 0:
            i = (i+1)%4
            x, y = nx, ny

    return answer

solution(4)