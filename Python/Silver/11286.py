# 우선순위 큐 : 절대값 힙
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
            a, b = heapq.heappop(h)
            print(b)
    else : 
        heapq.heappush(h, (abs(x), x))
