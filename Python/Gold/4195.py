# 유니온-파인드 : 친구 네트워크 (유니온 파인드 + 집합의 크기)
import sys
from collections import Counter
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for t in range(int(input())):
    f = int(input())
    parent = [i for i in range(2*f + 1)]
    id = {}
    cnt = 1

    for _ in range(f):
        person1, person2 = input().split()

        if person1 not in id:
            id[person1] = cnt
            cnt += 1
        if person2 not in id:
            id[person2] = cnt
            cnt += 1

        # parent[id[person1]] = find_parent(id[person1])
        # parent[id[person2]] = find_parent(id[person2])
        union_parent(parent, id[person1], id[person2])

        for i in range(1, cnt):
            parent[i] = find_parent(i)
        
        count = Counter(parent[1:cnt])
        print(count[parent[id[person1]]])
