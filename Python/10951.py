# 입력 조건 제한이 없으므로 예외처리 문제다.
import sys
input = sys.stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
