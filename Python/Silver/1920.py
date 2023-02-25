# 이분 탐색 : 수 찾기
import sys
input = sys.stdin.readline

n = int(input())

""" 집합을 이용한 풀이 1.
tmp = list(map(int, input().split()))
arr = set(tmp)

m = int(input())
lst = list(map(int, input().split()))

for l in lst:
    if l in arr:
        print(1)
    else:
        print(0)
"""

tmp = list(map(int, input().split()))
tmp.sort() # 이분 탐색을 위한 오름차순 정렬

m = int(input())
lst = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for l in lst:
    if binary_search(tmp, l, 0, n-1) == None:
        print(0)
    else:
        print(1)
