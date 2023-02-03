# 스택 1 : 스택 수열
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

flag = 0
cur = 1
stack, ans = [], []
for _ in range(n):
    num = int(input())
    
    while cur <= num:
        stack.append(cur)
        ans.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else :
        print("NO")
        flag = 1
        break

if flag == 0:
    print('\n'.join(ans))
