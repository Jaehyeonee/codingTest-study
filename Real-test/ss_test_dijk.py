import heapq
from collections import deque

q = deque()
N = int(input())
Maps = [list(map(int, input().split())) for _ in range(N)]
MAX_K = 5
INF = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(r1, c1, r2, c2):

    dist = [[[INF] * (MAX_K + 1) for _ in range(N)] for _ in range(N)]
    parent = [[[None] * (MAX_K + 1) for _ in range(N)] for _ in range(N)]
    hq = []

    sx, sy = r1, c1
    dist[sx][sy][1] = 0
    heapq.heappush(hq, (0, sx, sy, 1))  # (시간, x, y, k)

    while hq:
        time, x, y, k = heapq.heappop(hq)

        if (x, y) == (r2, c2) and Maps[x][y] == 0:
            path = []
            while True:
                path.append((x, y, k))
                prev = parent[x][y][k]
                if prev is None:
                    break
                x, y, k = prev
            path.reverse()
            return time, path

        # 1. 점프 능력 증가
        if k < MAX_K and dist[x][y][k + 1] > time + 1:
            dist[x][y][k + 1] = time + 1
            parent[x][y][k + 1] = (x, y, k)
            heapq.heappush(hq, (time + 1, x, y, k + 1))

        # 2. 점프 능력 감소
        if k > 1 and dist[x][y][k - 1] > time + 1:
            dist[x][y][k - 1] = time + 1
            parent[x][y][k - 1] = (x, y, k)
            heapq.heappush(hq, (time + 1, x, y, k - 1))

        # 3. 점프
        for dir in range(4):
            nx, ny = x, y
            for _ in range(k):
                nx += dx[dir]
                ny += dy[dir]
                if not (0 <= nx < N and 0 <= ny < N): break
                if Maps[nx][ny] == 1: break
            else:
                cost = time + k * k
                if Maps[nx][ny] == 0 and dist[nx][ny][k] > cost:
                    dist[nx][ny][k] = cost
                    parent[nx][ny][k] = (x, y, k)
                    heapq.heappush(hq, (cost, nx, ny, k))

    return -1

print(dijkstra(0, 0, 7, 7))
