# 큐, 덱 : 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])

ans = []
while len(queue) > 0:
    if len(queue) < k:
        tmp = queue[k % len(queue) -1]
    else:
        tmp = queue[k-1]
    queue.rotate(-k)
    queue.remove(tmp)
    ans.append(tmp)

print('<', end='')
print(', '.join(map(str,ans)), end='')
print('>', end='')
