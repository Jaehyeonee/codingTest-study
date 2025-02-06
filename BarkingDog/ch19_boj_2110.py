import sys
input = sys.stdin.readline
'''
 가장 인접한 두 공유기 사이의 최대 거리를 mid 로 설정하여, 이분 탐색을 진행
'''


n, c = map(int,input().strip().split())

coordinate = sorted([int(input()) for _ in range(n)])

min_distance = 1
max_distance = coordinate[-1] -coordinate[0] 

def binary_search(coordinate, min_distance, max_distance):
    while min_distance <= max_distance:
        mid = (min_distance + max_distance) //2
        current = coordinate[0]
        cnt = 1
        for i in range(1, n):
            if coordinate[i]-current >= mid:
                cnt +=1 
                current = coordinate[i]
        if cnt >= c :
            min_distance = mid + 1
            result = mid
        else:
            max_distance = mid - 1
        
    return result

print(binary_search(coordinate, min_distance, max_distance))



