# 이분 탐색 : 공유기 설치
import sys
input = sys.stdin.readline
n, c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0] # 가능한 거리의 최댓값

while start <= end:
    mid = (start + end) // 2

    # 첫 집 + mid 보다 크거나 같다 -> 설치 가능 / 안 되면 mid값 조정.
    cnt = 1
    current = arr[0] # 마지막으로 공유기 설치된 위치 저장
    for i in range(1, len(arr)):
        if current + mid <= arr[i]:
            cnt += 1
            current = arr[i]
    
    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
