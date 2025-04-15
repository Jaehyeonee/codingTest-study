T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    numbers = list(map(int, input().split()))
    for n in numbers:
        if n % 2 == 1:
            answer += n
    print(f'#{test_case}', answer)
            