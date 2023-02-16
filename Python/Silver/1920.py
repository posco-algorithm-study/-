# 이분 탐색 : 수 찾기
import sys
input = sys.stdin.readline

n = int(input())

tmp = list(map(int, input().split()))
arr = set(tmp)

m = int(input())
lst = list(map(int, input().split()))

for l in lst:
    if l in arr:
        print(1)
    else:
        print(0)
