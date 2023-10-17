# 떡볶이 떡 절단 문제
# 원하는 조건을 만족하는 가장 알맞은 값(최소/최대) => 최적화 찾기 => 이진탐색

N, M = list(map(int, input().split(' ')))
h = list(map(int, input().split()))

start = 0
end = max(h)

# 이진탐색
result = 0

while(start <= end):
    total = 0
    mid = (start + end)//2
    for i in h:
        if i > mid:
            total += i - mid
        
    if total < M:     # m을 만족하지 못할 때
        end = mid -1 
    else:
        result = mid
        start = mid + 1
        
print(result)


