# 17298 : 오큰수 (스택2)
"""
5.6.SAT.2023
오큰수 : 오른 쪽에 있고, 기준보다 큰 값중 가장 왼쪽에 있는 값
배열을 스캔하면서 한 번에 오큰수를 구해야 한다. 그러기 위해 배열의 오른쪽부터 역순으로 확인한다.
"""
a = int(input()) # MAX 100만
arr = list(map(int, input().split()))
result = [-1] * a # 오큰수를 넣을 list
stack = []

for idx, a in enumerate(reversed(arr)):
    while stack and stack[-1] <= a:
        stack.pop()

    if stack:
        result[idx] = stack[-1]

    stack.append(a)

print(' '.join(map(str, reversed(result))))
