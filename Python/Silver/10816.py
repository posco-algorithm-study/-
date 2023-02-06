from collections import Counter

n = int(input())
array = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

counter = Counter(array)

for d in data:
    print(counter[d], end=' ')
