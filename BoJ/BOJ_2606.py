#백준 2606
#연결되어있는 노드를 끝까지 탐색해야 하므로 DFS가 유리 

#컴퓨터 수
computers = int(input())
#연결된 컴퓨터 쌍의 수
pairs = int(input())

#2차원 배열에 연결되어 있는 쌍 담기
c_pairs=[[] for _ in range(computers+1)]

#방문 여부를 나타내는 배열로 0으로 초기화
visited = [0] * (computers+1)

for _ in range(pairs):
    a, b = map(int,input().split())
    c_pairs[a].append(b)
    c_pairs[b].append(a)

cnt = 0

def dfs(c_pairs, v, visited):
    global cnt
    visited[v] = 1
    for i in c_pairs[v]:
        if visited[i] != 1:
            cnt +=1
            dfs(c_pairs, i, visited)


dfs(c_pairs, 1, visited)
print(cnt)
