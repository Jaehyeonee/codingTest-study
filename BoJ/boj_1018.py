# 실버4
# 완전 탐색 -> 정사각형의 최소 개수를 구해야함. 
# (완전탐색 > 결과도출 : 브루트포스 알고리즘)
'''
🔹 시간 복잡도 분석
- 최대 50×50 보드
- 8×8 크기의 체스판을 검사 → (N-7) × (M-7)
- 내부에서 8×8을 비교 → O(8×8) = O(64)
>>>>>총 O((N-7) × (M-7) × 64) ≈ O(NM)

최대 연산 횟수: 50×50×64 = 160,000 (충분히 빠름)

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
# mxn 직사각형

board = [input().strip() for _ in range(n)]
print(board)

pattern1 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

pattern2 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

min_result = 64

        
for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        count2 = 0

        # 8*8로 띄어낸 애들에서 체스판이 되도록 최소 색칠 개수
        for x in range(8):
            for y in range(8):
                a = i+x
                b = j+y

                if board[a][b] != pattern1[x][y]:
                    print(board[a][b],pattern1[x][y] )
                    count1 += 1
                
                if board[i+x][j+y] != pattern2[x][y]:
                    print(board[i+x][j+y],pattern2[x][y] )
                    count2 += 1
        
        min_result = min(min_result, count1, count2)

print(min_result)

