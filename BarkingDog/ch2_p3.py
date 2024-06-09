'''
	n이 제곱수이면 1을 반환하고, 제곱수가 아니면 0을 반환
	n은 10억 이하의 자연수이다.
'''

def fun3(n):
	for i in range(1,n+1):
		if i*i == n:
			return 1
	return 0
	
print(fun3(9))