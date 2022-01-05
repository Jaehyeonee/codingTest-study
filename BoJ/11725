import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
#노드의 개수 입력
N=int(input())

#쌍 연결 저장 리스트 형성
pair=[[]*N for _ in range(N+1)]

#부모 노드 저장
parents=[0 for _ in range(N+1)]

#노드의 입력 쌍 입력
for i in range(N-1):
    a,b=map(int,input().split())
    #a에 대응->b원소, b에대응 ->a원소 각 리스트에 교차로 저장
    pair[a].append(b)
    pair[b].append(a)

#방문 dfs 정의
def dfs(pair,v,visited):
    #현재 노드와 연결된 다른 노드 방문
    for i in pair[v]:
        if visited[i]==0:
            visited[i]=v
            dfs(pair,i,visited)

dfs(pair,1,parents)

for i in range(2,N+1):
    print(parents[i])
