'''
<고려해야할 점>
1. cctv별로 감시 방향이 다름
2. cctv는 90도 방향으로 회전함.
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
                  #1    #2     #3     #4        #5
direction = [[], [1], [1,3], [0,1], [0,1,3], [0,1,2,3]]

cctv = []

def cal(rotate):
    visit = [[0]* m for _ in range(n)]
    for i in range(len(cctv)):
        si, sj = cctv[i]
        rot = rotate[i]
        types = graph[si][sj] # 1~5번 타입

        for dr in direction[types]:
            ci, cj = si, sj
            dr = (dr+rot) % 4
            while True:
                ci, cj = ci+dx[dr], cj+dy[dr]
                if not (0<= ci < n and 0<= cj <m):
                    break
                if graph[ci][cj] == 6:
                    break
                visit[ci][cj] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and visit[i][j] == 0:
                count+=1
    return count

def dfs(n, rotate):
    global ans
    if n == len(cctv):
        ans = min(ans, cal(rotate))
        return
    dfs(n+1, rotate+[0])
    dfs(n+1, rotate+[1])
    dfs(n+1, rotate+[2])
    dfs(n+1, rotate+[3])


for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv.append((i,j))
ans = n*m
dfs(0,[])
print(ans)