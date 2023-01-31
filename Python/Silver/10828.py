# 스택
import sys
input = sys.stdin.readline
n = int(input())

order = []
stack = []
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        stack.append(order[1])
    if order[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    if order[0] == 'size':
        print(len(stack))
    if order[0] == 'empty':
        if not stack: print(1)
        else : print(0)
    if order[0] == 'top':
        if not stack: print(-1)
        else: print(stack[-1])
