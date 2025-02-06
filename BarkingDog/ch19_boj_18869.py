import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
planet = [list(map(int, input().split())) for _ in range(m)]
dic = {}
new_space_list = [[] for _ in range(m)]
for i in range(m):
    sort_plan = sorted(list(set(planet[i])))
    for j in range(len(sort_plan)):
        dic[sort_plan[j]]=j
    for k in planet[i]:
        new_space_list[i].append(dic[k])

new_space_list.sort()
cnt, ans = 1, 0
for i in range(1, m):
    if new_space_list[i] == new_space_list[i - 1]:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        cnt = 1

ans += cnt * (cnt - 1) // 2
print(ans)





