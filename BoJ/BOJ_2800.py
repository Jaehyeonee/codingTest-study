express = input().strip()
ans = [] 
braces = []
open_idx = []

'''
point를 항상 -1로 고정하고 계속 감만 진행
braces.append([x, y])로 새 쌍을 추가하고 있지만, 
이 리스트에 대해 정확히 어떤 괄호가 마지막인지 point로 추적하지 못해.

올바른 방식으로는 스택을 활용
'''
# x, y = -1, -1
# for index, e in enumerate(express):
#     if e == '(':
#         x = index
#         braces.append([x,y])
#     if e == ')' :
#         braces[point][1] = index
#         point -= 1
    
'''
스택활용
'''

for index, e in enumerate(express):
    if e == '(':
        open_idx.append(index)
    elif e == ')':
        x = open_idx.pop()
        y = index
        braces.append((x,y))

result = set()
'''괄호 제거 조합 만들기'''
# 1부터 시작 : 공집합 제외
for mask in range(1, 1<<len(braces)):
    remove_comb = set()
    print(bin(mask,))
    for i in range(len(braces)):
        if mask & (1 << i):
            print(bin(mask) , bin((1 << i)))
            remove_comb.add(braces[i][0])
            remove_comb.add(braces[i][1])
    
    replace = ''
    for i in range(len(express)):
        if i not in remove_comb:
            replace += express[i]
    result.add(replace)
    
    
for r in sorted(result):
    print(r)
