# 잃어버린 괄호 : 모르겠어서 구글링 함
array = input().split('-') # 최소값 만들려면 무조건 -를 기준으로 나누어 괄호 치면 됨

tmp = []
for a in array:
    total_sum = 0
    numbers =  a.split('+')
    for number in numbers: # +로 묶인 애들끼리 더함
        total_sum += int(number)
    tmp.append(total_sum)

for i in range(1, len(tmp)):
    tmp[0] -= tmp[i] # 첫번째 숫자 - (덧셈으로 묶인애들 합)
print(tmp[0])
