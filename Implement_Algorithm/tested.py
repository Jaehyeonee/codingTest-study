
from collections import defaultdict

dic = defaultdict(list)
dic2 = defaultdict(list)
for _ in range(5):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic2[a].append(b)
    dic2[b].append(a)

print("dic: ", dic)
print("dic2: ", dic2)

