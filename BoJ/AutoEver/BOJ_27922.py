# 오토에버 기출 
# 유형: 정렬, 그리디 
# N개의 강의 중 K개만을 수강해서 2종류의 skill이 최대가 되도록 합의 최댓값 구하기
'''
예제:
N=3, K=2
    | a b c
강의1[2 4 10]
강의2[55 8 2]
강의3[1 9 5]
________________________
<풀이방법>
skill a,b,c 3개가 있을 때
강의별로 skill 조합인
case1: a+b
case2: a+c
case3: b+c
________________________
1) 각 강의별로 역량2개씩을 묶어서 정렬
2) 두개씩 묶은 역량 중에 값이 높은 순서대로 정렬되면,
      a+b  a+c  b+c
1순위| 강의2 강의2 강의1
2순위| 강의3 강의1 강의3
3순위| 강의1 강의3 강의2

3) 정렬된 리스트에서 K개를 선택해 해당 역량 2개의 합을 구함
---------------------k=2
(강의2,3) (강의2,1) (강의1,3)
=73      =69      =16
------------------------
(k=2)개의 강의를 수강했을 때,
얻을 수 있는 두 종류의 역량의 합의 최댓값
= 73
4) 역량 묶음 case중에 합이 가장 큰 걸 반환


'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lectures = []
for i in range(N):
    skill = list(map(int, input().split()))
    lectures.append(skill)

a = sorted(lectures, key = lambda x : -(x[0]+x[1]))
b = sorted(lectures, key = lambda x: -(x[0]+x[2]))
c = sorted(lectures, key = lambda x: -(x[1]+x[2]))

a_sum_b = 0
a_sum_c = 0
b_sum_c = 0

for i in range(K):
    a_sum_b += a[i][0]+a[i][1]
    a_sum_c += b[i][0]+b[i][2]
    b_sum_c += c[i][1]+c[i][2]

print(max(a_sum_b,a_sum_c,b_sum_c))