## -- Solution1 -- ##

#(x,y) 쌍의 개수 입력 받기
rows=int(input())

#2차원 배열 생성 (모든 요소 0)
arrLi=[[0 for col in range(2)] for row in range(rows)]
resLi=[[0 for col in range(2)] for row in range(rows)]

#입력 값 받기
for i in range(rows):
    a, b=input().split()
    arrLi[i][0]=int(a)
    arrLi[i][1]=int(b)

#arr[][1] 기준으로 정렬 후 arr[][0] 기준으로 정렬
#내림차순으로 정렬하고 싶으면 -x[0]으로 쓰기
resLi=sorted(arrLi, key=lambda x:(x[1], x[0]))

# print(arr[][0], arr[][1])을 출력하는 결과
for x, y in resLi:
    print(x, y)
    


## -- Solution2 -- ##

import sys

count=int(sys.stdin.readline().strip())

status=[]

#status 리스트안에 [x,y] 원소로 => 이중리스트 status 완성
for i in range(count):
    status.append(list(map(int,sys.stdin.readline().split(" "))))

#정렬 기준: 우선순위) y좌표 오름차순 -> x좌표 오름차순
#sort의 default는 오름차순이므로 reverse=False는 따로 안써줘도 무방
status.sort(key=lambda x: (x[1],x[0]))

for i in range(len(status)):
    print(status[i][0], status[i][1])
