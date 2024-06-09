n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(str, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [ [False] * m for _ in range(n) ]
answer = 0

def dfs(x, y):
    global chk
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or ice[x][y] == '1':
        return
    else:
        chk = 1
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        
for i in range(n):
    for j in range(m):
        chk = 0
        dfs(i, j)
        if chk == 1:
            answer += 1
print(answer)