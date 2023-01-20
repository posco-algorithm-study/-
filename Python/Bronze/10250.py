for _ in range(int(input())):
    h, w, n = map(int, input().split()) # 층, 방, 번째 손님
    
    xx, yy = divmod(n, h)

    if yy == 0:
        yy = n // xx
        xx -= 1

    print(str(yy) + str(xx+1).zfill(2))
