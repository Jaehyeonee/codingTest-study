# # 계수정렬
# import sys
# input = sys.stdin.readline

# ### 실패: 계수 정렬을 사용했으나 메모리 초과 > 아마 max를 사용하고 뒤에서부터 인덱스를 접근하는 것이 문제.
# n = int(input())

# num = list(int(input()) for _ in range(n))
# m = max(num) + 1
# count = [0] * m
# result = [0] * n

# for i in range(n):
#     count[num[i]] += 1

# for i in range(m):
#     if i >=1 :
#         count[i] = count[i-1] + count[i]


# for i in range(n-1,-1, -1):
#     c = count[num[i]]
#     result[c-1] = num[i]
#     count[num[i]] -= 1

# print(result)

### 성공: 올바른 계수 정렬
import sys
input = sys.stdin.readline

#계수정렬 활용
n = int(input())
arr = [0] * (10000 + 1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언

#각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1
  
#arr에 기록된 정보 확인
for i in range(len(arr)):
    if arr[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(i)