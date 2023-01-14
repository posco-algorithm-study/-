import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    num = int(input().rstrip())
    data.append(num)

avg = sum(data) / len(data)

data.sort()

middle = data[len(data) // 2]

c = Counter(data)
order = c.most_common() # 빈도가 높은 것부터 전부 반환, dict 형

# 최빈값이 하나일 때
if len(data) == 1 or order[0][1] > order[1][1] : 
    mostcommon = order[0][0]
# 최빈값이 두 개 이상일 때 두 번째로 작은 값 반환
else:
    tmp = []
    for i in range(len(order)):
        if order[i][1] == order[0][1]:
            tmp.append(order[i])
    tmp.sort()
    mostcommon = tmp[1][0]

print(round(avg))
print(middle)
print(mostcommon)
print(max(data) - min(data))
