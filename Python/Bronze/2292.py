# 점화식은 세웠으나 일반항 구하기 힘들어서 인터넷 사이트로 구함
n = int(input())

for i in range(1, n+1):
    tmp = 3 * pow(i, 2) - 3 * i + 2
    if tmp > n:
        print(i)
        break
