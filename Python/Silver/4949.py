# 스택 1 : 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
    array = list(input().rstrip())
    # 입력 종료 조건
    if array[0] == '.':
        break

    # 문장에서 괄호만 뽑아내 stack에 저장
    stack = []
    for a in array:
        if a == '(' or a == ')' or a == '[' or a == ']':
            stack.append(a)

    # 괄호 Check
    tmp = []
    ans = 'yes'
    # 첫 번째 괄호는 무조건 여는 것

    for s in stack:
        if stack[0] == ')' or stack[0] == ']':
            ans = 'no'
        # 스택 안의 여는 괄호 보다 닫는 괄호 수가 많을 수 없음
        if s == '(' or s == '[': tmp.append(s)
        # XXX : 여기 아래부터 수정
        elif s == ')' :
            if '(' not in tmp or tmp[-1] != '(':
                ans = "no"
                continue
            tmp.pop()
        elif s == ']' :
            if '[' not in tmp or tmp[-1] != '[':
                ans = "no"
                continue
            tmp.pop()
    
    if len(tmp) != 0:
        ans = "no"
    print(ans)
