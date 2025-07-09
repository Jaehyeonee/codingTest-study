from collections import Counter
import sys
input = sys.stdin.readline


# {'a':3, 'b':3}

def luckey(pre, current_length):
    answer = 0

    if current_length == len(s):
       return 1
        
    
    for key in count.keys():
        # a, b
        if key == pre or count[key] == 0:
            continue
        count[key] -= 1
        answer += luckey(key, current_length + 1)
        count[key] += 1
    
    return answer



s = input().rstrip()
count = Counter(s)
print(luckey('',0))

def DFS(K, P):
    global result
    
    if K == 0:
        result += 1
        return
        
    for i in range(26):
        if alph[i] > 0 and i != P:
            alph[i] -= 1
            DFS(K - 1, i)
            alph[i] += 1
 
            
S = list(input())
N = len(S)
 
result = 0
alph = [0] * 26
 
for i in range(N):
    alph[ord(S[i]) - 97] += 1
    
DFS(N, -1)
print(result)

