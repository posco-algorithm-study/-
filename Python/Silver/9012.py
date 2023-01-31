# 스택 1 : 괄호
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    array = list(input())
    stack = []
    ans = 'YES'
    for a in array:
        # 첫 번째 괄호는 무조건 여는 것
        if array[0] != '(':
            ans = 'NO'
            continue
        # 스택 안의 여는 괄호 보다 닫는 괄호 수가 많을 수 없음
        if a == '(' : stack.append(a)
        elif a == ')' :
            if not stack :
                ans = "NO"
                continue
            stack.pop()
    if len(stack) != 0:
        ans = "NO"
    print(ans)
"""
1. 첫번째는 무조건 여는 괄호일 것
2. 여는 괄호보다 닫는 괄호가 많을 수 없음
3. 마지막에 여는 괄호가 남아있으면 안 됨
"""
