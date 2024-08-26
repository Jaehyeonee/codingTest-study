import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    word = input().rstrip()
    if word in dic:
        continue
    else:
        dic[word] = len(word)

result = sorted(dic.items(), key=lambda x: (x[1],x[0]))

for i in range(len(result)):
    print(result[i][0])
    
    