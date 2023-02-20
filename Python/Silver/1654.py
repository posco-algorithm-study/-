# 이분 탐색 : 랜선 자르기
import sys
input = sys.stdin.readline
k, n = map(int, input().split())

lst = []
for _ in range(k):
    lst.append(int(input()))
lst.sort(reverse = True) # 랜선 길이 내림차순 정렬

start = 1
end = lst[0]
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for l in lst:
        cnt += l // mid
    
    if cnt < n :
        end = mid - 1
    else:
        start = mid + 1
        
print(end)
