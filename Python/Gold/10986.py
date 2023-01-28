# 나머지 합
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
count_module = [0 for _ in range(m)]
for a in array:
    sum_value += a
    count_module[sum_value % m] += 1

# print(count_module)
ans = count_module[0]
for v in count_module:
    ans += v * (v - 1) // 2
print(ans)
