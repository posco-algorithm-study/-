a, b, v = map(int, input().split())

day = (v - a) // (a - b)
x = (a - b) * day # 현재 위치

nx = x + a

if nx >= v:
    print(day + 1)
else:
    nx -= b # 밤
    x = nx
    print(day + 2)
