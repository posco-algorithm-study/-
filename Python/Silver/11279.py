# 우선순위 큐 : 최대 힙
import heapq
import sys
input = sys.stdin.readline

h = []
for _ in range(int(input())):
    x = int(input())
    if x == 0 :
        if not h:
            print(0)
        else:
            print(-heapq.heappop(h))
    else : 
        heapq.heappush(h, -x)
