import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

for i in range(len(array)):
    if array[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(array[i]):
            print(i)