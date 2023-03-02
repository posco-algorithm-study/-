# 최단 경로 : 숨바꼭질 3
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split()) # 5, 17
graph = [[] for _ in range(100001)]

for a in range(100001):
    if a != 100000:
        graph[a].append((a+1, 1))
    if a >= 1:
        graph[a].append((a-1, 1))
    if a <= 50000:
        graph[a].append((2*a, 0))

def Dijkstra(start, end):
    distance = [INF] * (100001)
    q = []
    heapq.heappush(q, (0,start))
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

    return distance[end]

print(Dijkstra(n, k))
