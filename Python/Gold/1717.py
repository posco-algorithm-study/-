# 유니온 파인드 : 집합의 표현
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return parent[x]

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x]=find_parent(parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# main
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    cal, a, b = map(int, input().split())   
    if cal == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
