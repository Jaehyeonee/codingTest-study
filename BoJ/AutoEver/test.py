import sys
input = sys.stdin.readline
from collections import deque, defaultdict


def solution(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * (n+1)  

    def bfs(start):
        queue = deque([start])
        visited[start] = 0
        count = [1, 0]
        is_bipartite = True 

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] == 1 - visited[node]
                    count[visited[neighbor]] += 1
                    queue.append(neighbor)

                elif visited[neighbor] == visited[node]:
                    is_bipartite = False
        return max(count) if is_bipartite else sum(count) // 2
    
    for i in range(1, n+1):
        if visited[i] == -1:
            max_nodes += bfs(i) if i in graph else 1

    return max_nodes


# n 정점 개수
n, m = map(int, input().split())
edges = [tuple(map(int,input().split())) for _ in range(m)]
print(solution(n, edges))