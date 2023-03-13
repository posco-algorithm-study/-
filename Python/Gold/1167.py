# 트리 : 트리의 지름
import sys
input = sys.stdin.readline

# HACK : y가 비용인데 정확히 뭐지??
def dfs(x, y):
    # 각 노드와 연결된 노드를 확인
    for a, b in graph[x]:
        # 탐색하지 않은 노드라면
        if visited[a] == -1:
            visited[a] = b + y # 탐색하기까지 걸린 간선의 거리로 초기화
            dfs(a, b + y) # 재귀적으로 탐색

v = int(input()) # 정점 개수
graph = [[] for _ in range(v+1)]

for _ in range(v):
    lst = list(map(int, input().split()))
    for i in range(1, len(lst)-2, 2):
        graph[lst[0]].append((lst[i], lst[i+1]))

visited = [-1] * (v+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited)) # 1번 노드에서 제일 먼 노드를 찾는다.
visited = [-1] * (v + 1)
visited[start] = 0
dfs(start, 0) # 1번 노드부터 가장 먼 노드에서 다시 제일 먼 노드를 찾는다.

# 트리의 지름 출력
print(max(visited))
