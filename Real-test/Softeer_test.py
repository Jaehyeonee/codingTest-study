# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

num = list(map(int, input().split()))


def sol(num):
	try:
		splitNum=list(map(str,num))
		splitNum.sort(key=lambda x : x*4, reverse=True)
		Max = int(''.join(map(str,splitNum)))

		splitNum.sort(key=lambda x : x*4, reverse=False)
		Min = int(''.join(map(str, splitNum)))

		result = Max+Min
		print(result)
	
	except:
		print(-1)

sol(num)
	
	
