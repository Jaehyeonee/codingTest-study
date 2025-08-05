import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


# y > row, x > col
for _ in range(R):
    for cy in range(min(N,M)//2): # 껍질 계산
        row, col = cy, cy
        prev_value = A[row][col]
        # 좌측 배열
        for d in range(cy+1, N-cy):
            row = d 
            nxt_val = A[row][col]
            A[row][col] = prev_value
            prev_value = nxt_val
            # print(A)
            
        # 하측 배열
        for d in range(cy+1, M-cy):
            col = d
            next_value = A[row][d]
            A[row][d] = prev_value
            prev_value = next_value
            # print(A)
        
        # 우측 배열
        for d in range(cy+1, N-cy):
            row = N-1-d
            nxt_val = A[row][col]
            A[row][col] = prev_value #16
            prev_value = nxt_val
            # print(A)
        
        # 상측 배열
        for d in range(cy+1, M-cy):
            col = M-1-d
            nxt_val = A[row][col]
            A[row][col] = prev_value
            prev_value = nxt_val

for a in A:
    print(*a)

            

        
        

            