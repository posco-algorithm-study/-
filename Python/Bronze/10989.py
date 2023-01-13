import sys
input = sys.stdin.readline
count = [0] * 10001

for _ in range(int(input())):
    count[int(input())] += 1

for i in range(1, len(count)):
    for j in range(count[i]):
        print(i)
# 제출은 pypy3 말고 python3로 할 것
