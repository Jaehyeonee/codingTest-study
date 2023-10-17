# 백준 1067 https://www.acmicpc.net/problem/1067
# N개의 수가 있는 X와 Y가 있다. 이때 X나 Y를 순환 이동시킬 수 있다. 순환 이동이란 마지막 원소를 제거하고 그 수를 맨 앞으로 다시 삽입하는 것을 말한다. 예를 들어, {1, 2, 3}을 순환 이동시키면 {3, 1, 2}가 될 것이고, {3, 1, 2}는 {2, 3, 1}이 된다. 순환 이동은 0번 또는 그 이상 할 수 있다. 
# 이 모든 순환 이동을 한 후에 점수를 구하면 된다. 점수 S는 다음과 같이 구한다.

# S = X[0]×Y[0] + X[1]×Y[1] + ... + X[N-1]×Y[N-1]


N = int(input())

S = 0


for i in range(N <= 60000):
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

for i in range (N):
    max_index = i
    for j in range(i+1, N):
        if(X[max_index] < X[j]):
            max_index = j
    X[i], X[max_index] = X[max_index], X[i]


for i in range (N):
    max_index = i
    for j in range(i+1, N):
        if(Y[max_index] < Y[j]):
            max_index = j
    Y[i], Y[max_index] = Y[max_index], Y[i]

for i in range(N):
    sb = X[i]*Y[i]
    S += sb

print(S)

