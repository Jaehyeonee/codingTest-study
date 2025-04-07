# solution1. 브루트 포스 >> 최적화X >> 시간 복잡도:  O(n^2)
from itertools import combinations
from functools import reduce
def solution1(fruit, k):
    answer = 0
    # itertools.combinations(fruit, k)을 사용하여 모든 경우의 수를 확인하고 있음.
    # N이 커질수록 조합의 개수가 기하급수적으로 증가하기 때문에 최적화를 하지 않는다면 완전탐색 방식으로 볼 수 있음.
    f = list(combinations(fruit, k))
    print(f)
    # 모든 가능한 OR 결과를 직접 모두 계산하고 set에 저장
    ans = set(bin(int(x, 2) | int(y, 2))[2:] for x, y in f)
    print(ans)
    answer = len(ans)
    return answer

# solution2. 불필요한 조합 탐색을 줄이고 이미 나온 OR결과 재활용
# 개선된 O(n^2)
def solution2(fruit, k):
    answer = set()

    fruit_int = [int(x, 2) for x in fruit]
    print(fruit_int)

    for comb in combinations(fruit_int, k):
        print(comb)
        # bit_or = reduce(lambda a, b: a|b, comb) 
        bit_or = comb[0]
        for n in comb[1:]:
            bit_or |= n
        answer.add(bin(bit_or)[2:]) # 2진수로 변환시 '0b'접두사가 붙어서 떼줘야 함
    print(answer)
    return

# soution3. 비트마스킹 (조합을 직접 생성하지 않도록)
# k개의 원소로 이루어진 모든 부분집합을 탐색하도록 함.

def solution3(fruit, k):
    answer = set()
    fruit_int = [int(x,2) for x in fruit]
    n = len(fruit_int)

    # 비트마스크로 모든 부분집합 탐색
    # ['1110' , '1100', '1001', '0011']
    '''
    4개의 원소에 대한 부분집합의 개수 = 2^n = 16개 (0000~1111)
    이때 비트마스크로 표현된 부분집합이 1001, 0011, 1010.. 이렇다면 원소가 2개 선택되었다는 뜻
    따라서 k=2이면, 부분집합 중에서도 2개의 원소가 선택된 부분집합이라는 뜻.
    '''
    # 0 부터 2^n-1까지 모든 부분집합 탐색을 뜻함 = n개의 요소에 대해 총 2^n개의 부분집합이 있음
    for mask in range(1 << n): 
        m = bin(mask)
        # 1의 개수를 셌는데, k와 동일하다는건 = k개의 원소를 선택한 부분집합 이라는 뜻
        if m.count('1') == k: 
            bit_or = 0
            for i in range(n):
                # # 1을 왼쪽으로 i칸 이동시킨다 , 1<<0 = 0001
                
                if mask & (1 << i): 
                    
                    bit_or |= fruit_int[i]
                    
            answer.add(bin(bit_or)[2:])

    return len(answer)



# ['1110' , '1100', '1001', '0011'] k=3
print(solution1(['1110' , '1100', '1001', '0011'], 2))
print('\n\n\n')
print(solution2(['1110' , '1100', '1001', '0011'], 3))
print(solution3(['110' , '100', '001', '001'], 3))