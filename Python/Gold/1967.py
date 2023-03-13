# 트리 : 트리의 지름
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def dfs(x, y):
    # 각 노드와 연결된 노드를 확인
    for a, b in graph[x]:
        # 탐색하지 않은 노드라면
        if visited[a] == -1:
            visited[a] = b + y # 탐색하기까지 걸린 간선의 거리로 초기화
            dfs(a, b + y) # 재귀적으로 탐색

n = int(input()) # 정점 개수
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited)) # 1번 노드에서 제일 먼 노드를 찾는다.
visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0) # 1번 노드부터 가장 먼 노드에서 다시 제일 먼 노드를 찾는다.

# 트리의 지름 출력
print(max(visited))
