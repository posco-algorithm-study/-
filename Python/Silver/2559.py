# 수열 : for문 중첩해도, 안 해도 시간초과 뜸 -> 배열에서 max 구하지 않기 + 슬라이싱 쓰지 않고 메모제이션 쓰기
n, k = map(int, input().split())
temp = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for t in temp:
    sum_value += t
    prefix_sum.append(sum_value)

tmp = []
for i in range(n, k-1, -1):
    tmp.append(prefix_sum[i] - prefix_sum[i-k])
print(max(tmp))
