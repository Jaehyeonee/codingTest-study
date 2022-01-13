# 시간초과의 이유를 don't know
# 시간초과 이유 찾음: https://jjangsungwon.tistory.com/44

import sys

num=int(input())
intArr=[]
resArr=[]

intArr=sys.stdin.readline().split()
intArr=list(map(int, intArr))

for i in range(num-1, -1, -1):
    j=i-1
    reception=intArr[j]
    while(reception<intArr[i] and j>=0):
        j=j-1
        reception=intArr[j]

    if (j>=0):
        resArr.insert(0, j+1)
    else:
        resArr.insert(0, 0)

for i in resArr:
    print(i, end=" ")
