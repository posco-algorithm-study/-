a, b = map(int, input().split())

a = [int(x) for x in str(a)]
b = [int(x) for x in str(b)]

a[0], a[2] = a[2], a[0]
b[0], b[2] = b[2], b[0]
a = a[0] * 100 + a[1] * 10 + a[2]
b = b[0] * 100 + b[1] * 10 + b[2]

if a > b:
    print(a)
else:
    print(b)
