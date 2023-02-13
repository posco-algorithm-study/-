# 큐, 덱 : 회전하는 큐
from collections import deque

n, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
data = list(map(int, input().split()))

cnt = 0
for d in data:
    while True:    
        if d == queue[0]:
            queue.popleft()
            break
        else:
            # 왼쪽이 더 가까우면 rotate right
            if queue.index(d) <= len(queue) // 2 :
                queue.rotate(-1)
                cnt +=1
            # 오른쪽이 더 가까우면 rotate left
            else:
                queue.rotate(1)
                cnt +=1

print(cnt)
