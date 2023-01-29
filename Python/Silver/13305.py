# 주유소
n = int(input())

road = list(map(int, input().split())) # n-1개
city = list(map(int, input().split())) # n개
city.pop() # 도착지에서는 주유 안 하니까 빼버림
price = 0

start, end, idx = 0, 0, 0
while end < n-1:
    if city[start] <= city[end]:
        price += city[start] * road[idx]
    else:
        price += city[idx] * road[idx]
        start = idx
    idx += 1
    end += 1

print(price)
