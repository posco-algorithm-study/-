# 집합과 맵 : 서로 다른 부분 문자열의 개수
s = input()
ans = set()

for i in range(len(s)): # 0 ~ s-1까지 s번 반복
    for j in range(i, len(s)):
        temp = s[i:j+1]
        ans.add(temp)

print(len(ans))
