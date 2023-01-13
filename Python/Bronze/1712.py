a, b, c = map(int, input().split())

n = 0
if c != b: # 분모가 0이 되지 않도록
    n = int(a / (c-b)) + 1
if n <= 0:
    print(-1)
else:
    print(n)
