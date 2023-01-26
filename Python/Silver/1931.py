# 회의실 배정 30분 고민하다 안돼서 해결방법 봄
n = int(input())

array = []
for _ in range(n):
    start, end = map(int, input().split())
    array.append([start, end])

array.sort(key = lambda x: x[0]) # 종료시간이 같을 때, x가 작은 값이 먼저 오도록 하려고
# 윗 줄은 그냥 array.sort()만 해도 될듯
array.sort(key = lambda x: x[1])

cnt = 1
end = array[0][1] # 가장 작은 end값
for i in range(1, n):
    if array[i][0] >= end: # 다음 회의 시간이 안 겹치면
        cnt += 1
        end = array[i][1]

print(cnt)
