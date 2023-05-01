"""
틀린 이유 : 최단경로가 여러 개 존재할 경우, g-h를 지나는 경로도 있고 g-h를 지나지 않는 경로도 있는데 그 경우가 고려 안됨.
해결 :
s, g, h, x를 기준으로 구간을 3개 지정해
각 구간의 최단 cost 합이 s~x까지 최단경로 cost와 같은지 비교.
이때, g-h 순서도 있고 h-g순서도 있음. 둘 다 고려할 것.
구간 1: s-g 또는 s-h
구간 2: g-h
구간 3: h-x 또는 g-x
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
    return distance[end] - distance[start]

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    ans = []
    for _ in range(t):
        x = int(input())
        s_to_g = dijkstra(s, g)
        g_to_h = dijkstra(g, h)
        h_to_x = dijkstra(h, x)

        s_to_h = dijkstra(s, h)
        h_to_g = dijkstra(h, g)
        g_to_x = dijkstra(g, x)
        
        if s_to_g + g_to_h + h_to_x == dijkstra(s, x) or s_to_h + h_to_g + g_to_x == dijkstra(s, x):
            ans.append(x)        
        
    ans.sort()
    print(' '.join(map(str,ans)))
