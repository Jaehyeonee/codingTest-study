import sys
import heapq
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        producers = []
        consumers = []

        for _ in range(n):
            x, c = map(int, input().split())
            if c > 0:
                producers.append([x, c])
            else:
                consumers.append((x, -c))

        producers.sort(key=lambda x: abs(x[0]))  # 가까운 순 정렬
        total_distance = 0

        for cx, demand in consumers:
            # 최소 거리 저장
            min_dist = float('inf')
            visited = {}

            def dfs(pos, dist, taken, left):
                nonlocal min_dist
                state = (pos, taken, tuple(left))
                if state in visited and visited[state] <= dist:
                    return
                visited[state] = dist

                if taken >= demand:
                    min_dist = min(min_dist, dist + abs(pos - cx))
                    return

                for i in range(len(producers)):
                    px, pc = producers[i]
                    if left[i] == 0:
                        continue

                    move = abs(pos - px)
                    take = min(demand - taken, left[i])

                    left[i] -= take
                    dfs(px, dist + move, taken + take, left)
                    left[i] += take  # backtrack

            initial_left = [p[1] for p in producers]
            dfs(0, 0, 0, initial_left)
            total_distance += min_dist

        print(total_distance)
solve()        
# def solve():

#     T = int(input())
#     for _ in range(T):
#         n = int(input())
#         producers = []
#         consumers = []

#         for _ in range(n):
#             x, c = map(int, input().split())
#             if c > 0:
#                 producers.append([x, c])  # 리스트로 수정: 도시락 수량 업데이트 가능
#             else:
#                 consumers.append((x, -c))

#         total_distance = 0

#         for cx, demand in consumers:
#             min_dist = float('inf')

#             def dfs(cur_pos, acc_dist, taken, producer_left):
#                 nonlocal min_dist

#                 if taken >= demand:
#                     acc_dist += abs(cur_pos - cx)
#                     min_dist = min(min_dist, acc_dist)
#                     return

#                 for i in range(len(producers)):
#                     px, pc = producers[i]
#                     if producer_left[i] == 0:
#                         continue

#                     move_dist = abs(cur_pos - px)
#                     take = min(demand - taken, producer_left[i])

#                     producer_left[i] -= take
#                     dfs(px, acc_dist + move_dist, taken + take, producer_left)
#                     producer_left[i] += take  # 백트래킹

#             producer_left = [p[1] for p in producers]
#             dfs(0, 0, 0, producer_left)
#             total_distance += min_dist

#         print(total_distance)

