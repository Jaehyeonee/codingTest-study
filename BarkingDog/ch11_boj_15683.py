import sys
input = sys.stdin.readline
# 북, 동 남 서

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = [[], [1], [1,3],[0,1],[0,1,3],[0,1,2,3]]

def cal(rotate):
    visit = [[0]*m for _ in range(n)]

    for i in range(cnt):
        si, sj = cctv[i]
        rot = rotate[i]        # 0-3 회전
        types = graph[si][sj]  # cctv 종류 1~5
        # 모든 CCTV에 대해 모든 방향으로 뻗어가면서 방문 표시
        for dr in direction[types]:
            ci, cj = si, sj
            dr = (dr+rot)%4
            while True:
                ci, cj = ci+dx[dr], cj+dy[dr]
                
                if not (0 <= ci < n and 0 <= cj < m):
                    break
                if graph[ci][cj] == 6 :
                        break
                visit[ci][cj]=1
    # 사각지대 0 이고 미방문 개수 카운트
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and visit[i][j] == 0:
                count+=1
    return count


def dfs(n, rotate):
    global ans
    if n == cnt:
        ans = min(ans,cal(rotate))
        return
    dfs(n+1, rotate+[0])  # 0
    dfs(n+1, rotate+[1])  # 90
    dfs(n+1, rotate+[2])  # 180
    dfs(n+1, rotate+[3])  # 270

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv.append((i,j))

cnt = len(cctv)
ans = n*m
dfs(0, [])
print(ans)


