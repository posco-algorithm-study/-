# 기본 수학 2 : 베르트랑 공준
import math

def is_prinme_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if is_prinme_number(i) == True:
            cnt += 1
    print(cnt)
