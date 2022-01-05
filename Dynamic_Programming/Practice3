# 인접한 창고 털기 불가능.
# i번째 창고: i-1 창고가 안 털렸을 때 털기 가능
#             i-2 창고가 털리면 털기 가능
#             i-3 창고부터는 노 상관

n=int(input())
arr=list(map(int, input().split()))

d=[0]*100  

# 다이나믹 프로그래밍

d[0]=arr[0]

d[1]=max(array[0], arr[1])  # 0과 1번째 창고 중 더 큰 것 털기

for i in range(2, n):
    
    # 전 창고 털기 VS 전전 창고와 해당 창고 털기
    d[i]=max(d[i-1], d[i-2]+arr[i])  

print(d[n-1])
