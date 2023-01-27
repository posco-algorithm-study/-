from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

nth_sum = []
for _ in range(m):
    i, j = map(int, input().split())
    nth_sum.append(prefix_sum[j] - prefix_sum[i-1])

for i in range(len(nth_sum)):
    print(nth_sum[i])
