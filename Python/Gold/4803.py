# 트리 : 트리 (그래프가 주어졌을 때 트리인지 판별)
import sys
from collections import Counter
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

case_num = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    parent = [0] * (n+1)

    for i in range(1, n+1):
        parent[i] = i

    cycled_child = set([])
    for _ in range(m): # 간선 정보 입력받기
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

        if find_parent(parent, a) == find_parent(parent, b):
            cycled_child.update(graph[a], graph[b])
        else:
            union_parent(parent, a, b)

    # 나중에 연결된 간선은 갱신 안 되는 경우가 있어서 추가로 한 번 더 돌림
    for i in range(1, n+1):
        parent[i] = find_parent(parent, i)
    parent_set = set(parent[1:])

    # 만약, cycled_child의 부모 노드가 parent에 있을 경우 제거
    for c in cycled_child:
        if parent[c] in parent_set:
            parent_set.remove(parent[c])

    tree_cnt = len(Counter(parent_set))

    if tree_cnt > 1:
        print("Case {}: A forest of {} trees.".format(case_num, tree_cnt))
    elif tree_cnt == 1:
        print("Case {}: There is one tree.".format(case_num))
    else:
        print("Case {}: No trees.".format(case_num))
    case_num += 1
