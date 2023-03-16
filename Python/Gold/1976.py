# 유니온 파인드 : 여행 가자
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]

for i in range(1, n+1):
    graph[i] = list(map(int, input().split()))
plan = set(map(int, input().split()))

for i in range(1, n+1):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i, j+1)
            union_parent(parent, j+1, i)

# 부모 노드 업데이트
for i in range(1, n+1):
        parent[i] = find_parent(parent, i)

goal = set([])
for p in plan:
    goal.add(parent[p])

print("YES" if len(goal) == 1 else "NO")
