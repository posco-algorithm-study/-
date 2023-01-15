import sys
n = int(sys.stdin.readline())

num = list(map(int, input().split()))
num_sort = sorted(set(num)) # 중복값 제거 & 오름차순 정렬

# 딕셔너리에 가장 작은 수부터 ~ 큰 수까지 0 ~ N-1 값으로 치환 (그저 크기 비교만 할 거니까)
final = {num_sort[i] : i for i in range(len(num_sort))}

for i in num:
    print(final[i], end=' ')
