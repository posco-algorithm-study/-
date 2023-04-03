# 최소 신장 트리 : 다리 만들기 2 (삼성 A형 기출문제)
from collections import Counter

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

edges = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 1. 먼저 DFS로 섬을 구분짓는다.
visited = [[0] * m for _ in range(n)]
island = 1
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0 # 방문처리
        visited[x][y] = island
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

obstacle = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            obstacle += 1
            island += 1

parent = [i for i in range(island)]

# 지도 확인용 코드, 제출시 주석처리할 것
# for v in visited:
#    print(v)

# 2. 각 섬마다 다른 섬과의 거리(2이상)를 간선으로 저장해 트리 생성
# a) 가로 다리 계산
for i in range(n):
    counter = Counter(visited[i]) # Set으로 변경 가능
    # 한 줄(가로)에 섬이 두 개 이상 존재하면 거리 계산
    if len(counter) > 2:
        first = visited[i].index(0)
        while True:
            cost = 0
            for j in range(first, m):
                if j == m-1 and visited[i][j] == 0:
                    cost = 0
                    right = j
                    break
                if visited[i][j] == 0:
                    cost += 1
                else:
                    left = first - 1
                    right = j
                    break
            if cost >= 2 and left != -1:
                a = visited[i][left]
                b = visited[i][right]
                edges.append((cost, a, b))
                # print('가로:', a, '와', b, '연결 = 비용은 :', cost)

            if visited[i][right:].count(0) < 2 or right == m - 1:
                break
            else:
                first = visited[i].index(0, right)

# print()

# b) 세로 다리 계산 : 2차원 배열을 90도 회전
new = [[0] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        new[j][n-i-1] = visited[i][j]

for i in range(m):
    counter = Counter(new[i]) # Set으로 변경 가능
    # 한 줄(가로)에 섬이 두 개 이상 존재하면 거리 계산
    if len(counter) > 2:
        # 0이 연속 등장할 때, 양 옆에 섬이 존재하면 edges에 추가
        first = new[i].index(0)
        while True:
            cost = 0
            for j in range(first, n):
                if j == n-1 and new[i][j] == 0:
                    cost = 0
                    right = j
                    break
                if new[i][j] == 0:
                    cost += 1
                else:
                    left = first - 1
                    right = j
                    break
            if cost >= 2 and left != -1:
                a = new[i][left]
                b = new[i][right]
                edges.append((cost, a, b))
                # print('세로:', a, '와', b, '연결 = 비용은 :', cost)

            if new[i][right:].count(0) < 2 or right == n - 1:
                break
            else:
                first = new[i].index(0, right)

# 비용 오름차순 정렬
edges.sort()

# 3. MST
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 부모 노드 업데이트
for i in range(1, len(parent)):
        parent[i] = find_parent(parent, i)
    
if len(set(parent[1:])) != 1:
    print(-1)
else:
    print(result)
