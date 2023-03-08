# 트리 : 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                parent[i] = v
                queue.append(i)
                visited[i] = True

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [1] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited)

for i in range(2, n+1):
    print(parent[i])
