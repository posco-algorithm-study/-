# 유니온-파인드 : 사이클 게임
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

# def find_parent(x):
#     while x != parent[x]:
#         x = parent[x]
#     return x

def union_parent(parent, a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n)]

cycle = False
for i in range(m):
    a, b = map(int, input().split())
    # 사이클 존재
    if find_parent(a) == find_parent(b) and cycle == False:
        cycle = i+1
    union_parent(parent, a, b)
if not cycle: print(0)
else: print(cycle)
