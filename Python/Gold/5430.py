# 큐, 덱 : AC
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):

    order = list(input().rstrip()) # 명령어 문자열
    n = int(input())
    lst = input().rstrip()[1:-1]
    arr = deque(lst.split(','))

    # 배열에 정수가 없을 경우 '' -> 이 문자 지워주기 위해 clear함
    if n == 0:
        arr = []

    flag = 0
    R_flag = 0
    for o in order:
        if o == 'R' and R_flag == 0:
            R_flag = 1
        elif o == 'R' and R_flag == 1:
            R_flag = 0

        if o == 'D':
            if not arr:
                print('error')
                flag = 1
                break

            if R_flag == 1:
                arr.pop()
            else:
                arr.popleft()

    if flag != 1 and R_flag == 0:
        print('[' + ','.join(arr) + ']')
    if flag != 1 and R_flag == 1:
        arr.reverse()
        print('[' + ','.join(arr) + ']')
