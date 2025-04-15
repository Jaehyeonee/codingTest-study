# from collections import deque
#
# q = deque()
# N = int(input())
# Maps = [list(map(int, input().split())) for _ in range(N)]
#
# def solve(r1, c1, r2, c2):
#     k = 1
#     max_k = 5
#     time = 0
#
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#
#     visited = [[[False] * (max_k + 1) for _ in range(N)] for _ in range(N)]
#     parent = [[[None] * (max_k + 1) for _ in range(N)] for _ in range(N)]
#
#     q.append((r1, c1, k, time))
#     visited[r1][c1][k] = True
#
#     while q:
#         x, y, k, time = q.popleft()
#         # print(x, y, k, time)
#
#         if (x, y) == (r2, c2) and Maps[x][y] == 0:
#             # 경로 추적
#             path = []
#             while True:
#                 path.append((x, y, k))
#                 prev = parent[x][y][k]
#                 if prev is None:
#                     break
#                 x, y, k = prev
#             path.reverse()
#             print("경로:")
#             for step in path:
#                 print(step)
#             return time
#
#         # 1. k 증가
#         if k < max_k and not visited[x][y][k+1]:
#             visited[x][y][k+1] = True
#             parent[x][y][k+1] = (x, y, k)
#             q.append((x, y, k+1, time+1))
#
#         # 2. k 감소
#         if k > 1 and not visited[x][y][k-1]:
#             visited[x][y][k-1] = True
#             parent[x][y][k-1] = (x, y, k)
#             q.append((x, y, k-1, time+1))
#
#         # 3. 점프
#         for d in range(4):
#             nx, ny = x, y
#             for _ in range(k):
#                 nx += dx[d]
#                 ny += dy[d]
#
#                 if not(0 <= nx < N and 0 <= ny < N):
#                     break
#                 if Maps[nx][ny] == 1:
#                     break
#             else:
#                 if Maps[nx][ny] == 0 and not visited[nx][ny][k]:
#                     visited[nx][ny][k] = True
#                     parent[nx][ny][k] = (x, y, k)
#                     q.append((nx, ny, k, time+pow(k,2)))
#
#     return -1
#
# print("최소 시간:", solve(0, 0, 7, 7))

# # 2025년 상반기 samsung sds 코테 문제 복기
# '''
# 용사 문제 : 시뮬레이션 + bfs
# '''
from collections import deque

q = deque()
N = int(input())
Maps = [list(map(int, input().split())) for _ in range(N)]

def solve(r1, c1, r2, c2):
    k = 1
    max_k = 5
    time = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[[False] * (max_k + 1) for _ in range(N)] for _ in range(N)]
    parent = [[[None] * (max_k + 1) for _ in range(N)] for _ in range(N)]
    q.append((r1, c1, k, time))
    visited[r1][c1][k] = True

    while len(q)!=0:
        x, y, k, time = q.popleft()
        # print(x, y, k, time)
        if (x, y) == (r2, c2):
            # path = []
            # while True:
            #     path.append((x, y, k))
            #     prev = parent[x][y][k]
            #     if prev is None:
            #         break
            #     x, y, k = prev
            # path.reverse()
            # print('경로\n')
            # for step in path:
            #     print(step)
            return time

        if k < max_k and not visited[x][y][k+1]:
            visited[x][y][k+1] = True
            parent[x][y][k + 1] = (x, y, k)
            q.append((x, y, k+1, time+1))

        if k > 1 and not visited[x][y][k-1]:
            visited[x][y][k-1] = True
            parent[x][y][k - 1] = (x, y, k)
            q.append((x, y, k-1, time+1))

        for d in range(4):
            nx, ny = x, y
            # blocked = False

            for _ in range(k):
                nx = nx+dx[d]
                ny = ny+dy[d]

                if not(0 <= nx < N and 0 <= ny < N) :
                    break
                if Maps[nx][ny] == 1:
                    break

            else:
                if Maps[nx][ny] == 0 and not visited[nx][ny][k]:
                    visited[nx][ny][k] = True
                    parent[nx][ny][k] = (x, y, k)
                    q.append((nx, ny, k, time+pow(k,2)))

    return -1

print(solve(0, 0, 7, 7))