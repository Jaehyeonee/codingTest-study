#시간초과 문제 해결 아직 못함

from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

#쌍 연결 저장 리스트 형성
pair=[[]*N for _ in range(N+1)]

#부모 노드 저장
parents=[0 for _ in range(N+1)]

#노드의 입력 쌍 입력
for i in range(M):
    a,b=map(int,input().split())
    pair[b].append(a)

#방문 bfs 정의
def bfs(pair,start):
    queue=deque([start])
    #visited 초기화
    visited=[False]*(N+1)

    #현재 노드를 방문처리
    visited[start]=True

    #횟수 세는 변수 
    global count
    count=1

    #큐가 비어있을 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        #해당 원소와 연결된 방문안된 원소 큐에 삽입
        for i in pair[v]:
            if not visited[i]:
                count +=1
                queue.append(i)
                visited[i]=True

    return count

ranks=[0 for _ in range(N+1)]

for i in range(1,N+1):
    ranks[i]=bfs(pair,i)

#순위 비교
for i in range(1,N+1):
    if ranks[i] == max(ranks):
        print(i, end=" ")
