MAX = 4473
x = int(input())

# 대각선끼리 방 만들기
# n == 1: 1/1
# n == 2: 2/1 1/2 (3번째, 2번째)
# n == 3: 3/1 2/2 1/3 (4, 5, 6번째)
# n == 4: 4/1 3/2 2/3 1/4 (7, 8, 9, 10번째)
# 1, 3, 6, 10, 15... -> an = n + n*(n-1)/2

an = []
for i in range(MAX):
    a = int(i + i * (i - 1) / 2)
    an.append(a)

for i in range(len(an)):
    if an[i] < x <= an[i + 1]: # 여기 IndexError
        n = i + 1
        break

son = 0
mother = 0

# 해당 방 안의 번째들 (예 : 3번 방 안에는 4,5,6번째 수가 있음)
floor = [x for x in range(an[n-1] + 1, an[n]+1)]

for idx, f in enumerate(floor):
    if x == f:
        mother = 1 + idx
        son = len(floor) - mother + 1

if n % 2 != 0:
    print('{}/{}'.format(son, mother))
else:
    print('{}/{}'.format(mother, son))
