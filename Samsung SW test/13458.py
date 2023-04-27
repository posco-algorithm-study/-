n = int(input())
examinee = list(map(int, input().split()))

b, c = map(int, input().split()) # 총감독관(한 고사장 당 한 명만 가능), 부감독관
# 총감독관은 반드시 한 명 이상 각 고사장에 있어야 하는듯

result = 0
for exam in examinee:
    if exam >= b: # 총 감독관 한 명
        result += 1
    else:
        result += 1
        continue
    tmp = exam - b
    result += tmp // c
    if tmp % c > 0:
        result += 1

print(result)
