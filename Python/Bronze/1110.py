n = int(input())
start = n
cnt = 0

while True:
    if n < 10:
        tmp = [0, n]
        n = 10 * n + tmp[1]
    else:
        lst = [int(x) for x in str(n)]
        tmp = lst[0] + lst[1]
        if tmp < 10:
            tmp = [0, tmp]
        else:
            tmp = [int(x) for x in str(tmp)]
        n = lst[1] * 10 + tmp[1]

    cnt += 1

    if n == start:
        break

print(cnt)
