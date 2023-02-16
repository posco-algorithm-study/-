import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemon = dict()
for idx in range(1, n+1):
    tmp = input().rstrip()
    pokemon[idx] = tmp
    pokemon[tmp] = idx

for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(pokemon[int(q)])
    else:
        print(pokemon[q])
