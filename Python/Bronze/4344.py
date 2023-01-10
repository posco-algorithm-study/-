c = int(input())

for _ in range(c):
    array = list(map(int, input().split()))
    avg = sum(array[1:])/array[0]
    
    cnt = 0
    for a in array:
        if a == array[0]:
            continue
        if a > avg:
            cnt += 1
        
    ratio = cnt / array[0] * 100
    print('{:.3f}%'.format(round(ratio, 3)))
