# 이분 탐색 : 가장 긴 증가하는 부분 수열 2 (LIS)
n = int(input())
arr = list(map(int, input().split()))
tmp = [0] # memozation list

for a in arr:
    if tmp[-1] < a:
        tmp.append(a)
    else:
        start = 0
        end = len(tmp)

        while start < end:
            mid = (start + end) // 2

            if tmp[mid] < a:
                start = mid + 1
            else:
                end = mid
        tmp[end] = a
            
print(len(tmp) - 1) # 맨 처음 0을 제외해야 하니까
