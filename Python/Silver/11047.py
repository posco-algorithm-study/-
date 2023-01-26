# 동전 0
n, x = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

cnt = 0
for c in coin:
    if c <= x:
        cnt += x // c
        x %= c
    
    if x == 0:
        break

print(cnt)
