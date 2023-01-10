# 리스트 요소끼리 뺄셈하기 -> zip과 리스트 컴프리헨션으로 해결
ans = [1, 1, 2, 2, 2, 8]
lst = list(map(int, input().split()))
result = [ansi - lsti for ansi, lsti in zip(ans, lst)]
print(*result)
