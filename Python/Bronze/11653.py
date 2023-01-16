# 기본 수학 2 : 소인수분해
import math
def factorization(number):
    d = 2

    while d <= number:
        if number % d == 0:
            print(d)
            number //=  d
        else:
            d += 1

factorization(int(input()))
