import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

list_a = deque(map(int, input().split()))
list_b = deque(map(int, input().split()))

result = deque()



while list_a and list_b:
    if list_a[0] > list_b[0]:
        result.append(list_b.popleft())
    else:
        result.append(list_a.popleft())

ans = result + list_a + list_b

print(' '.join(map(str, ans)))

