n = int(input())

array = []
for idx in range(n):
    age, name = input().split()
    age = int(age)
    array.append((age, idx, name))

array.sort()

for a in array:
    print(a[0], a[2])
