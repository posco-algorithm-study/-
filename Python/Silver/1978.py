# 기본 수학 2 : 소수 찾기
import math

n = int(input())

def is_prinme_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

array = list(map(int, input().split()))

cnt = 0
for a in array:
    if is_prinme_number(a) == True:
        cnt += 1
print(cnt)
