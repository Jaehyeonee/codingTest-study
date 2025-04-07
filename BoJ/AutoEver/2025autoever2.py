import sys
from itertools import permutations

# 입력 받기
def read_input():
    n, k, p = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arrow_power = list(map(int, sys.stdin.readline().split()))
    return n, k, p, grid, arrow_power

# 특정 위치 (x, y)에서 화살을 맞췄을 때 얻는 점수 계산
def get_score(grid, n, x, y, radius):
    total_score = 0
    visited = set()
    
    for i in range(n):
        for j in range(n):
            if abs(x - i) + abs(y - j) < radius:  # 맨해튼 거리 조건
                visited.add((i, j))
                total_score += grid[i][j]
    
    return total_score

# 백트래킹을 이용한 최소 힘 탐색
def dfs(grid, n, arrows, index, score, total_force, p, min_force):
    if score == p:  # 정확한 점수 도달
        return min(min_force, total_force)

    if score > p or index >= len(arrows):  # 점수를 초과하거나 모든 화살 사용 완료
        return min_force

    # 현재 화살의 반경
    radius = arrows[index]

    # 모든 좌표를 탐색
    for i in range(n):
        for j in range(n):
            new_score = get_score(grid, n, i, j, radius)
            
            # 다음 상태 탐색 (중복 방문 허용)
            min_force = dfs(grid, n, arrows, index + 1, score + new_score, total_force + radius, p, min_force)

    return min_force

# 메인 실행 함수
def solve():
    n, k, p, grid, arrow_power = read_input()
    arrow_power.sort()  # 작은 힘부터 탐색하여 최적해 찾기
    min_force = dfs(grid, n, arrow_power, 0, 0, 0, p, float('inf'))
    
    print(min_force if min_force != float('inf') else -1)

if __name__ == "__main__":
    solve()
