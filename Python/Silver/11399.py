# ATM
n = int(input())
data = list(map(int, input().split()))
data.sort()

tmp = []
for i in range(1, n+1):
    tmp.append(sum(data[:i]))

print(sum(tmp))
