import sys
input = sys.stdin.readline

n, c = map(int,input().split())
array = list(map(int, input().split()))
dic = {}

for i in array:
    if i in dic:
        dic[i] +=1 
    else:
        dic[i] = 1

result = sorted(dic.items(), key = lambda x: x[1], reverse= True)


for key, value in result:
    for _ in range(value):
        print(str(key), end=' ')