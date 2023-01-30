# 구간 합 구하기 5
n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

coord = []
for _ in range(m):
    coord.append(list(map(int, input().split()))) # (x1, y1) ~ (x2, y2)

# 행 방향
prefix_sum = []
for j in range(n):
    sum_value = 0
    tmp = []
    for i in range(n):
        sum_value += array[j][i]
        tmp.append(sum_value)
    prefix_sum.append(tmp)

# 열 방향
ans = [[0] * (n+1) for _ in range(n+1)]
for j in range(1, n+1):
    sum_value = 0
    for i in range(1, n+1):
        sum_value += prefix_sum[i-1][j-1]
        ans[i][j] = sum_value

for c in coord:
    x1, y1, x2, y2 = c
    result = ans[x2][y2] - ans[x1-1][y2] - ans[x2][y1-1] + ans[x1-1][y1-1]
    print(result)
