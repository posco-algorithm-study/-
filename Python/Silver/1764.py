n, m = map(int,input().split())

listen, see = set(), set()
for _ in range(n):
    listen.add(input())
for _ in range(m):
    see.add(input())

cnt = 0
name = listen.intersection(see)

print(len(name))
print('\n'.join(sorted(name)))
