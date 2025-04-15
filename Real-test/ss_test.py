from collections import deque
# you
q = deque()
N = int(input())
Maps = [list(map(int, input().split())) for _ in range(N)]
MAX_K = 5
INF = float('inf')

def solve(r1, c1, r2, c2):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[[INF] * (MAX_K + 1) for _ in range(N)] for _ in range(N)]
    parent = [[[None] * (MAX_K + 1) for _ in range(N)] for _ in range(N)]
    q = deque()

    sx, sy = r1, c1
    dist[sx][sy][1] = 0
    q.append((sx, sy, 1))

    while q:
        x, y, k = q.popleft()
        time = dist[x][y][k]

        # 1. k 증가
        if k < MAX_K and dist[x][y][k + 1] > time + 1:
            dist[x][y][k + 1] = time + 1
            parent[x][y][k + 1] = (x, y, k)
            q.append((x, y, k + 1))

        # 2. k 감소
        if k > 1 and dist[x][y][k - 1] > time + 1:
            dist[x][y][k - 1] = time + 1
            parent[x][y][k - 1] = (x, y, k)
            q.append((x, y, k - 1))

        # 3. 점프
        for dir in range(4):
            nx, ny = x, y
            for _ in range(k):
                nx += dx[dir]
                ny += dy[dir]
                if not (0 <= nx < N and 0 <= ny < N):
                    break
                if Maps[nx][ny] == 1:
                    break
            else:
                if Maps[nx][ny] == 0 and dist[nx][ny][k] > time + k * k:
                    dist[nx][ny][k] = time + k * k
                    parent[nx][ny][k] = (x, y, k)
                    q.append((nx, ny, k))

    # 🔍 도착 지점의 모든 k 중 최소 시간 찾기
    ex, ey = r2, c2
    min_time = INF
    best_k = -1
    for k in range(1, MAX_K + 1):
        if dist[ex][ey][k] < min_time:
            min_time = dist[ex][ey][k]
            best_k = k

    # # 경로 복원
    if min_time == INF:
        return -1

    path = []
    x, y, k = ex, ey, best_k
    while True:
        path.append((x, y, k))
        prev = parent[x][y][k]
        if prev is None:
            break
        x, y, k = prev
    path.reverse()

    return min_time, path

print(solve(1, 0, 1, 3))