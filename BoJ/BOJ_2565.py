# 💡 bisect란?
# a = [1,3,5,7]
# print(bisect.bisect_left(a,4))
# print(bisect.bisect_right(a,4))

# bisect.bisect_left(a,9)
# bisect.insort(1,)

''' < 전깃줄 문제 >
dp 구현 = O(n^2)
bisect 구현 = O(nlogn)

'''

import sys
import bisect
input = sys.stdin.readline

n = int(input())
wires = [tuple(map(int, input().split())) for _ in range(n)]

# A 기준 정렬
wires.sort()

'''✅. DP로 구현'''

dp = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(n - max(dp))



'''✅. bisect로 풀기'''

lis = []
b = [b for (a,b) in wires]

for num in b:
    idx = bisect.bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(n - len(lis))





'''
⭐️ 문제 변형 
교차하지 않기 위해 없애야하는 전깃줄의 종류 모든 조합 출력하기
ex. output : [(1,8),(3,9),(4,1)], [(1,8),(2,2),(3,9)]

tip -> LIS [최장 증가 부분 수열]을 구하고, LIS에 포함되지 않은 값을 출력
'''


b_values = [b for a, b in wires]

# DP: LIS 길이 저장
dp = [1] * n
for i in range(n):
    for j in range(i):
        if b_values[j] < b_values[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# LIS 최대 길이
max_len = max(dp)

# 경로 추적 함수 (모든 LIS 조합 찾기)
results = []
def dfs(idx, path):
    if dp[idx] == 1:
        results.append([idx] + path)
        return
    for prev in range(idx):
        if b_values[prev] < b_values[idx] and dp[prev] == dp[idx] - 1:
            dfs(prev, [idx] + path)

# 시작점: dp[i] == max_len 인 모든 인덱스에서 역추적 시작
for i in range(n):
    if dp[i] == max_len:
        dfs(i, [])

# 출력: 각 LIS 조합마다 제거 대상 구하기
printed = set()
for path in results:
    lis_indices = set(path)
    removed = tuple(wires[i] for i in range(n) if i not in lis_indices)
    if removed not in printed:
        printed.add(removed)
        print("제거 대상:", removed)

'''
------------------------------------------------------------------------
'''

n = int(input())
wires = [tuple(map(int, input().split())) for _ in range(n)]
wires.sort()  # A 기준 정렬
b = [b for a, b in wires]

# DP: LIS 길이 + 경로 저장
dp = [1] * n
routes = [[] for _ in range(n)]

for i in range(n):
    routes[i] = [[i]]  # 자기 자신으로 시작
    for j in range(i):
        if b[j] < b[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                routes[i] = [route + [i] for route in routes[j]]
            elif dp[j] + 1 == dp[i]:
                routes[i] += [route + [i] for route in routes[j]]

# LIS 최대 길이
max_len = max(dp)

# 모든 LIS 경로 모음
all_lis = []
for i in range(n):
    if dp[i] == max_len:
        all_lis += routes[i]

# LIS 경로들 기반 제거 대상 출력
printed = set()
for lis in all_lis:
    remove = tuple(wires[i] for i in range(n) if i not in lis)
    if remove not in printed:
        printed.add(remove)
        print("제거 대상:", remove)
