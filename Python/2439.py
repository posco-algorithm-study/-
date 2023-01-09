# 문자열 오른쪽 정렬
n = int(input())

for i in range(1, n+1):
    chr = str('*' * i)
    print(chr.rjust(n))
