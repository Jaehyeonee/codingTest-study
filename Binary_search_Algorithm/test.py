import sys
# from collections import defaultdict, Counter


# input = sys.stdin.readline

# arr = list(map(int, input().split()))

# #  5 5 5 3 1 1 2 3 9 10 5
# dic = defaultdict(int)
# for i in arr:
#     dic[i] += 1

# print(dic)

# # 키 값을 기준으로 정렬
# dics = sorted(dic.items())
# print(dic.items())
# dicsv = sorted(dic.items(), key = lambda x : x[1], reverse= True )

# print(dics)
# print(dicsv)

# counts = Counter(arr)
# print("counts:", counts)

# result = []
# for i in dicsv:
#     result.append(i[0])

# print(result)

'''
import ast
coord = input().strip()
# numbers = [int(num) for num in coord if num.isdigit()]
# print(numbers)

coord_list = ast.literal_eval(coord)
print('coord_list', coord_list)

tuples = list(tuple(coord) for coord in coord_list)

print(tuples)


'''

import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    # start로 부터의 거리 값을 저장
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 # 시작은 0 값
    queue = []
    heapq.heappush(queue, [distances[start], start])
    print(heapq)

    while queue:
        # 탐색할 노드, 거리 가져옴
        current_distance, current_destination = heapq.heappop(queue)
        
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                # 다음 인접 거리 계산을 위해 큐에 삽입
                heapq.heappush(queue, [distance, new_destination])

    return distances
print(dijkstra(graph, 'A'))