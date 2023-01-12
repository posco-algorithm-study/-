import sys
input = sys.stdin.readline

words = input().rstrip() # 여기 rstrip() 안 해줘서 런타임 에러 났었음. 숫자일 땐 괜찮아도 문자열 할 땐 의식적으로 써주자
words = list(words.upper())

w = []
for word in words:
    if word not in w:
        w.append(word)

num = []
for i in w:
    num.append(words.count(i))

if num.count(max(num)) == 1:
    print(w[num.index(max(num))])
else:
    print('?')
