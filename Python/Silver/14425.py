n, m = map(int, input().split())

array = set()
for _ in range(n):
    array.add(input())
    
data = []
for _ in range(m):
    data.append(input())

cnt = 0
for d in data:
    if d in array:
        cnt += 1

print(cnt)
