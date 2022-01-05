num=int(input())
d=[0]*30001   # 입력 값의 범위만큼 
    
# 다이나막 프로그래밍 진행 (Bottom-Up)
# 최소의 수가 d[i]에 저장
for i in range(2, num+1):

    # 현재 수에서 -1
    d[i]=d[i-1]+1

    # 현재 수가 2로 나누어 떨어짐
    if (i%2==0):
        d[i]=min(d[i], d[i//2]+1)
        
    # 현재 수가 3로 나누어 떨어짐
    if (i%3==0):
        d[i]=min(d[i], d[i//3]+1)

    # 현재 수가 5로 나누어 떨어짐
    if (i%5==0):
        d[i]=min(d[i], d[i//5]+1)

print(d[num])

## ---- Another Solution ----

import sys
x = int(sys.stdin.readline().rstrip())

dp=[0]*30001
#2인덱스 부터 x+1인덱스 까지 범위 지정
for i in range(2, x+1):
    dp[i]  = dp[i-1]+1  #끝에 1을 더하는 이유는 함수의 호출 횟수를 구하기 위함
    
    if i % 5==0:
        dp[i] = min(dp[i], dp[i//5]+1)  # 두 수 중 더 적은 수를 구하고자 min함수 사용
    elif i % 3 ==0:
        dp[i] = min(dp[i], dp[i//3]+1)
    elif i%2 ==0:
        dp[i]= min(dp[i], dp[i//2]+1)


print(dp[x])
