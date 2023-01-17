# 기본 수학 2 : 골드바흐의 추측
import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

prime = [0] * (10001)
for i in range(10000):
    if is_prime_number(i) == True:
        prime[i] = i

for _ in range(int(input())):
    n = int(input())

    for i in range(n//2, 1, -1):
        if n - prime[i] in prime and prime[i] <= n - prime[i]:
            print(prime[i], n - prime[i])
            break
