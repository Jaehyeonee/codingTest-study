# https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC5-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-12865-%ED%8F%89%EB%B2%94%ED%95%9C%EB%B0%B0%EB%82%AD
# 유형 : DP
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
pack = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(K+1):
        weight = pack[i-1][0] # 현재 물건 무게
        value = pack[i-1][1]  # 현재 물건 가치
        if j >= weight: # 최대무게 j가 현재 물건 무게보다 큰경우
            dp[i][j] = max(dp[i-1][j] , value + dp[i-1][j-weight]) 
            # value + dp[i-1][j-weight]: (최대무게j-현재 물건 무게)로 남은 무게만큼의 가치도 더해줌
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])