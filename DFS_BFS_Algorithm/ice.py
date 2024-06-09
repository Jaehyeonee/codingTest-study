# import time
# welcome = input("'Merry Christmas'라고 입력해보세요! \n")

# if welcome == 'Merry Christmas':
#     for i in range(1,10):
#         time.sleep(0.5)
#         for k in range(10-i):
#             print(' ',end='')
#         for k in range(2*i-1):
#             print('*', end='')
        
# DFS : 깊이 우선 탐색 >   멀리있는 경우의 수 부터 확인 > 스택 > LIFO > 재귀함수
# BFS : 너비 우선 탐색 >   가까운 경우의 수 부터 확인 > 큐 > FIFO > 빠름

# dfs lifo stack으로 구현 => 재귀함수 

n, m = map(int, input().split())

graph = []
for i in range(n):
    d = list(map(int, input()))
    graph.append(d)


def dfs(x,y):
    if x < 0 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    
    
count=0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count+=1
print(count)


# def dfs(graph, v, visited):
    
#     #v는 시작위치
#     visited[v] = True
#     print(v , end = ' ')
    
#     #현재 노드와 연결된 노드를 재귀적으로 호출
#     for i in graph[v]:
#         if not visited[i]:
#             # print(visited)
#             dfs(graph, i, visited)
    
# graph = [
#     [],
#     [2,3,7],
#     [1,4,6],
#     [1,5, 7],
#     [2,6],
#     [3,7],
#     [2,4],
#     [1,3]
# ]

# #각 노드가 방문한 정보를 리스트 자료형으로 표현
# visited = [False] * 9

# print("방문순서")
# dfs(graph, 1, visited)