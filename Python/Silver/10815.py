import sys
input = sys.stdin.readline

n = int(input())
array = set(map(int, input().split()))
m = int(input())
card = set(map(int, input().split()))

ans = []
for c in card:
    if c in array : ans.append(1)
    else : ans.append(0)

print(*ans)
