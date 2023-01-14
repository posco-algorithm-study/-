import sys
input = sys.stdin.readline
n = int(input())

words = []
for _ in range(n):
    w = input().rstrip()
    words.append((len(w), w))

words.sort()

tmp = []
for i in range(n):
    tmp.append(words[i][1])

for idx, t in enumerate(tmp):
    if t in tmp[idx+1:]:
        continue
    print(t)
