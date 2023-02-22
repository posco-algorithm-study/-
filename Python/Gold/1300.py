# 이분 탐색 : k번째 수
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = k # B가 가질 수 있는 최댓값
while start <= end:
    mid = (start + end) // 2
    
    tmp = 0
    # 여기 for문이 잘 이해가 안 감
    for i in range(1, n+1) :
        tmp += min(mid // i, n)

    if tmp < k :
        start = mid + 1
    elif tmp >= k :
        ans = mid
        end = mid - 1

print(ans)
