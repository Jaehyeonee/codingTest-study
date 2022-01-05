n, m = map(int(input.split()))
value=[]


for i in range(n):
    value.append(int(input()))

d=[1001]*(m+1)

d[0]=0
for i in range(n):
    for j in range(value[i], m+1):
        if d[j-value[i]] != 1001:
            d[j] = min(d[j], d[j-value[i]]+1)

if d[m] == 1001:
    print(-1)
else:
    print(d[m])
