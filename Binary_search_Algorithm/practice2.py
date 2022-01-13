# 이코테 스터디 '이진탐색 알고리즘' - 2.부품찾기



n = int(input())

shop_data = list(map(int,input().split()))
shop_data.sort()


#guest request product
m = int(input())
guest_data = list(map(int, input().split()))

    

#이진탐색 
def binary_search(shop_data, target, start, end):
    if(start>end):
        return None
    mid =(start+end)//2

    if shop_data[mid] == target:
        return mid
    elif shop_data[mid] > target:
        return binary_search(shop_data, target, start, mid-1)
    else:
        return binary_search(shop_data, target, mid+1, end)


for i in guest_data:
    result = binary_search(shop_data, i, 0, n-1)
    if result != None:
        print("yes", end=' ')

    else:
        print("no" , end=' ')
