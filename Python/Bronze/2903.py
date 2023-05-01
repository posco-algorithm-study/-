"""
해당 문제는 Softeer Level 2 : 지도 자동 구축과 동일
"""

# 풀이 1. DP
n = int(input())

# DP Table
d = [0] * (n+1)
d[0] = 4

for i in range(1, n+1):
    d[i] = 2*(d[i-1]-1)

result = d[n-1] * 2 ** n + 1
print(result)

# 풀이 2. 수학 규칙
n = int(input())
a = 2
for _ in range(n):
    a += a - 1
print(a**2)
