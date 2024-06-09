'''
	n이하의 수 중에서 가장 큰 2의 거듭제곱수를 반환하는 함수를 작성해라
	n은 10억 이하의 자연수이다.
'''

def func4(n):
	i = 1
	while 2 * i <= n:
		i *= 2
		return i
		
print(func4(1024))