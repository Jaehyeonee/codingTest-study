'''
https://www.acmicpc.net/problem/1475
'''
import sys
input = sys.stdin.readline
word = str(input().strip())
ans = [0] * 10


for i in range(len(word)):
    num = int(word[i])
    
    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1

map()
print(max(ans))




