# 최단 경로 : 운동 (사이클 판별)
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]

# for a in range(1, v+1):
#     for b in range(1, v+1):
#         if a == b:
#             graph[a][b] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

k = v # k는 최종 도착지
for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 자기 자신 -> 자기 자신으로 돌아오는 거리 중 최소값 출력
ans = INF
for i in range(1, v+1):
    ans = min(ans, graph[i][i])

if ans >= INF:
    print(-1)
else:
    print(ans)
