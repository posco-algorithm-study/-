# 이분 탐색 : 나무 자르기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse = True)

start = 1
end = trees[0]
while start <= end:
    mid = (start + end) // 2

    total = 0
    for tree in trees:
        if tree > mid:
            total += (tree - mid)
    
    if total < m :
        end = mid - 1
    else:
        start = mid + 1

print(end)
