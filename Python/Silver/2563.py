LENGTH = 100
array = [[0] * LENGTH for _ in range(LENGTH)]

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1

result = 0
for a in array:
    result += sum(a)
print(result)
