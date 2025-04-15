'''
⭐️ tip : 빙고에서 가로세로대각선 구현 / 리스트 컴프리헨션
call을 2차원 5*5로 받지 않고, 
그냥 하나의 1차원배열 call = []로 받고 싶을 때 -> ```list comprehension```

<방법 1. call 리스트에 map 객체의 요소를 가져다가 extend(+=) 해주는 개념 >
call = []
test = map(int, input().split())
for _ in range(5):
    call += map(int,input().split())

<방법 2. 리스트 컴프리헨션 기법으로 한 줄로 구현>
calls = [int(x) for _ in range(5) for x in input().split()]
print(calls)
'''

# 빙고 문제 > 최대한 5로 고정하지 않고 나중에 N이 될수 있을 때를 고려
def count_bingo(colored):
    count = 0
    # 가로
    count += sum(1 for row in colored if sum(row) == 5)
    # 세로
    count += sum(1 for col in zip(*colored) if sum(col) == 5)
    # 대각선 ↘
    if all(colored[i][i] == 1 for i in range(5)):
        count += 1
    # 대각선 ↙
    if all(colored[i][4 - i] == 1 for i in range(5)):
        count += 1
    return count

def mark_and_check(check, cnt):
    for i in range(5):
        for j in range(5):
            if board[i][j] == check:
                colored[i][j] = 1
                if count_bingo(colored) >= 3:
                    print(cnt)
                    return True
                return False
    return False

def main():
    cnt = 0
    for i in range(5):
        for j in range(5):
            cnt += 1
            if mark_and_check(people[i][j], cnt):
                return  # 여기서 함수 종료로 프로그램 종료

# 입력
board = [list(map(int, input().split())) for _ in range(5)]
people = [list(map(int, input().split())) for _ in range(5)]
colored = [[0] * 5 for _ in range(5)]

main()
