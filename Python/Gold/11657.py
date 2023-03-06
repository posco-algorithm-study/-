# 최단 경로 : 타임머신 (벨만 포드)
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)

edges = []
for _ in range(m):
    s, d, w = map(int, input().split())
    edges.append((s, d, w))

def bellman_ford(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    for i in range(n):
        for s, d, w in edges:
            if dist[s] != INF and dist[d] > dist[s] + w:
                if i == n - 1:
                    return -1
                dist[d] = dist[s] + w
    return dist
 
dist = bellman_ford(1)
if dist == -1:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] >= INF:
            print(-1)
        else:
            print(dist[i])
