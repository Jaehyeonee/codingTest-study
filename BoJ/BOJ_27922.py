import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lectures = []
for i in range(N):
    skill = list(map(int, input().split()))
    lectures.append(skill)
first = sorted(lectures, key=lambda x: -(x[0] + x[1]))
second = sorted(lectures, key=lambda x: -(x[0] + x[2]))
third = sorted(lectures, key=lambda x: -(x[1] + x[2]))
 
a = sorted(lectures, key = lambda x : -(x[0]+x[1]))
b = sorted(lectures, key = lambda x: -(x[0]+x[2]))
c = sorted(lectures, key = lambda x: -(x[1]+x[2]))

print(a)
print(b)
print(c)

a_sum_b = 0
a_sum_c = 0
b_sum_c = 0

for i in range(K):
    a_sum_b += a[i][0]+a[i][1]
    a_sum_c += b[i][0]+b[i][2]
    b_sum_c += c[i][1]+c[i][2]

print(max(a_sum_b,a_sum_c,b_sum_c))