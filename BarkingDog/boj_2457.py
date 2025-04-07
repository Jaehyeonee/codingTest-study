
'''
그리디 : 공주님의 정원
'''

import sys
input = sys.stdin.readline

n = int(input())
flowers = list(list(map(int, input().split())) for _ in range(n))
flowers.sort()
print(flowers)

current = (3, 1)
i = 0
result = 0

while i < n :
    sm, sd, em, ed = flowers[i]
    if (sm, sd) <= current < (em, ed):
        max_end = (em, ed)
        while i < n-1 :
            nsm, nsd, nsem, nsed = flowers[i+1]
            if current < (nsm, nsd):
                break
            if max_end < (nsem, nsed):
                max_end = (nsem, nsed)
            i+=1

        result += 1
        current = max_end

        if (11, 30) < current:
            print(result)
            exit(0)

    i += 1
print(0)


        

            