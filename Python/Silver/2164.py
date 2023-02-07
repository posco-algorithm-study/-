# 큐, 덱 : 카드 2
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque([])
for i in range(1, n+1):
    queue.append(i)

for i in range(len(queue)-1):
    queue.popleft()
    queue.append(queue.popleft())

print(*queue)
