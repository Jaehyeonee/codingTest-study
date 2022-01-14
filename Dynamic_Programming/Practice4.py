n=int(input())

d=[0]*1001

d[1]=1
d[2]=3
for i in range(3, n+1):
		# 결과 값이 커질 수 있어서?? %796796 (걍 조건)
    d[i]=(d[i-1]+2*d[i-2])%796796  

print(d[n])
