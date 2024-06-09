# n 이하의 자연수 중에서 3의 배수이거나 5의 배수인 수를 모두 합한 값을 반환하는 함수 작성
# n은 10만 이하의 자연수이다

import sys
input = sys.stdin.readline

n = int(input())
result  = 0
for i in range(1, n+1):
    if i%3 == 0 or i%5 ==0:
        result+=i
    
print(result)

