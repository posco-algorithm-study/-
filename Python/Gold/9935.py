# 9935 : 문자열 폭발
words = input()
bomb = input()

stack = []
for i in range(len(words)):
    stack.append(words[i])
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
