# '''
# 2025 현대오토에버 상반기 코테 1번 문항
# 난이도 : 골드 4-3

# 📍전략
# 1. 이분그래프
# - 연결 요소별로 BFS를 이용해 2개의 그룹으로 나눔
# - 같은 그룹에 속한 노드는 서로 인접하지 않음
# - 더 많은 노드를 포함하는 그룹을 선택
# 2. 홀수 길이 사이클 처리
# - 홀수 길이의 사이클(ex.삼각형)이 존재하면 이분 그래프가 아님.
# - 홀수 길이의 사이클이 있으면 최대 독립 집합 크기를 하나 줄임.


# 📌 알고리즘 구현
# 1️⃣ BFS로 연결 요소 탐색 및 독립 집합 크기 계산
# 방문하지 않은 노드를 시작점으로 BFS 실행.
# 두 개의 그룹(0, 1)으로 나누면서 탐색.
# 각 그룹의 크기를 count[0], count[1]로 기록.
# 최종적으로 max(count[0], count[1])을 선택.
# 2️⃣ 사이클 감지 및 홀수 길이 체크
# BFS 탐색 중, 이미 방문한 노드를 다시 방문하는 경우 사이클 발생.
# 부모 노드 정보를 저장하여 사이클의 길이를 확인.
# 홀수 길이의 사이클이면 max(count) - 1을 적용하여 최대 선택 가능 개수를 줄임.

# 📌 홀수 길이 사이클이란?
# 사이클(= 한 점에서 출발해서 다시 돌아오는 경로)이 홀수 개의 정점으로 이루어진 경우를 의미.
# 예를 들어, 1 - 2 - 3 - 1처럼 정점이 **3개(홀수 개)**로 구성된 사이클이 있으면, 이분 그래프가 될 수 없음.
# 반면, 1 - 2 - 3 - 4 - 1처럼 정점이 **4개(짝수 개)**로 구성된 사이클은 이분 그래프가 됨.



# 📌 이분 그래프 (Bipartite Graph)란?
# ***이분 그래프란 모든 정점을 두 개의 그룹으로 나눌 수 있으며***
# , 같은 그룹에 속한 정점끼리는 서로 연결되지 않는 그래프입니다.
# 즉, 그래프의 모든 간선이 두 그룹을 연결하는 형태가 되어야 합니다.

# 🔹 이분 그래프의 핵심 조건
# ✅ 모든 정점을 두 개의 그룹으로 나눌 수 있어야 함
# ✅ 같은 그룹에 속한 정점끼리는 간선이 연결되지 않아야 함
# ✅ 홀수 길이의 사이클(3, 5, 7, ...)이 존재하면 이분 그래프가 될 수 없음


# 2️⃣ 이분 그래프 판별 방법 (BFS or DFS)
# 이분 그래프 여부를 판별하는 대표적인 방법은 BFS 또는 DFS를 사용한 색칠(2색 칠하기) 기법입니다.
# 즉, 시작 정점을 한 색(A)로 칠하고, 인접한 정점을 반대 색(B)로 칠하면서 진행합니다.


# '''


import sys
from collections import deque, defaultdict

def max_independent_set(n, edges):
    graph = defaultdict(list)

    # 그래프 구성
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * (n + 1)  # -1: 미방문, 0 또는 1: 두 그룹
    max_nodes = 0  

    def bfs(start):
        queue = deque([start])
        visited[start] = 0  # 첫 노드는 그룹 0
        count = [1, 0]  # [그룹 0 개수, 그룹 1 개수]
        is_bipartite = True  

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if visited[neighbor] == -1:  # 방문 안 했으면
                    visited[neighbor] = 1 - visited[node]  # 반대 그룹 배정
                    count[visited[neighbor]] += 1
                    queue.append(neighbor)
                elif visited[neighbor] == visited[node]:  # 같은 그룹이면 이분 그래프 아님
                    is_bipartite = False  

        return max(count) if is_bipartite else sum(count) // 2  # 홀수 길이 사이클 포함이면 ⌊n/2⌋만 선택 가능

    # 연결 요소별 탐색
    for i in range(1, n + 1):
        if visited[i] == -1:  # 방문 안 한 정점이면 BFS 수행
            max_nodes += bfs(i) if i in graph else 1  # 간선 없는 노드는 혼자 선택 가능

    return max_nodes

# 입력 처리
if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(max_independent_set(n, edges))


# import sys
# from collections import deque, defaultdict

# def max_independent_set(n, edges):
#     graph = defaultdict(list)
    
#     for u, v in edges:
#         graph[u].append(v)
#         graph[v].append(u)

#     visited = [-1] * (n + 1)  # 방문 여부 및 그룹 체크
#     max_nodes = 0  

#     def bfs(start):
#         queue = deque([start])
#         visited[start] = 0  # 첫 노드는 그룹 0
#         count = [1, 0]  # 두 그룹의 개수 (0번 그룹, 1번 그룹)
#         parent = {start: -1}  # 부모 정보 저장 (사이클 감지용)
#         cycle_length = float('inf')

#         while queue:
#             node = queue.popleft()
#             for neighbor in graph[node]:
#                 if visited[neighbor] == -1:  # 미방문 노드
#                     visited[neighbor] = 1 - visited[node]  # 반대 그룹 할당
#                     count[visited[neighbor]] += 1
#                     queue.append(neighbor)
#                     parent[neighbor] = node
#                 elif parent[node] != neighbor:  # 사이클 감지
#                     cycle_length = min(cycle_length, abs(visited[node] - visited[neighbor]) + 1)

#         # 홀수 사이클이 존재하는 경우 조정 (최대 선택 가능한 개수 줄이기)
#         if cycle_length % 2 == 1:
#             return max(count) - 1
#         return max(count)

#     # 연결 요소별 탐색
#     for i in range(1, n + 1):
#         if visited[i] == -1:  # 방문하지 않은 정점이면 BFS 수행
#             max_nodes += bfs(i) if i in graph else 1  # 간선이 없는 정점은 단독 선택 가능

#     return max_nodes

# # 입력 처리
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n, m = map(int, input().split())
#     edges = [tuple(map(int, input().split())) for _ in range(m)]
#     print(max_independent_set(n, edges))
