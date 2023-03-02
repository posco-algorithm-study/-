import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)] # n+1 주의
# 최단거리 테이블
distance = [INF] * (n+1)

for _ in range(m):
    # a에서 b로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = [] # 우선순위 큐를 위한 빈 리스트
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 인접 노드 확인 / i[0] : 인접 노드 , i[1] : 비용
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
