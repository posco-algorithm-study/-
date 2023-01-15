n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

sum_total = [[c + d for c, d in zip(a, b)] for a, b in zip(a,b)]

for s in sum_total:
    print(*s)
