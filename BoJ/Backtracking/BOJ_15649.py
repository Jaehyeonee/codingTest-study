# https://www.acmicpc.net/problem/15649
# 백트래킹 문제 기본 1)



def solution():

    if len(array) == m:
        print(" ".join(map(str, array)))
        return
    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            solution()
            array.pop()



n, m = map(int, input().split())
array=[]
solution()