import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

v  = [[0]*m for _  in range(n)]


def tetrimino(count, current, tmp):
    global answer

    if count == 4:
        answer = max(tmp, answer)
        return 
    
    for cx, cy in current:
        for i in range(4):
            nx , ny = cx+dx[i], cy+dy[i]

            if 0 <= nx < n and 0<= ny < m and v[nx][ny] == 0 :
                v[nx][ny] = 1
                tetrimino(count+1, current + [(nx,ny)], tmp+paper[nx][ny])
                v[nx][ny] = 0

    
answer = 0
for i in range(n):
    for j in range(m):
        v[i][j] = 1
        tetrimino(1,[(i,j)], paper[i][j])
print(answer)

    