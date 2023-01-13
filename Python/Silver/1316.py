import sys
input = sys.stdin.readline
n = int(input())

def group_word(array):
    for idx, num in enumerate(array):
        tmp = []
        if array.count(num) == 1:
            continue
        
        else:
            first_idx = array.index(num)
            array.reverse()
            final_idx = len(array) - array.index(num)
            array.reverse() # 원래대로 원위치

            tmp = array[first_idx : final_idx]

            if tmp.count(num) != len(tmp):
                return False
    
    return True

cnt = 0
for _ in range(n):
    data = list(input().rstrip())
    if group_word(data) == True:
        cnt += 1

print(cnt)
