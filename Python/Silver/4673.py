MAX = 10000

def self_number(num):
    lst = [int(x) for x in str(num)]
    dn = sum(lst) + num
    return dn

numbers = [i for i in range(1, MAX+1)]
tmp = []

for i in range(1, MAX+1):
    tmp.append(self_number(i))

for i in range(1, MAX+1):
    if i not in tmp:
        print(i)

# 테스트 중이던 print부분을 안 지우고 그냥 제출해서 틀렸음. 원래대로라면 1트라이 정답!
# 질문 목록을 죽 훑어보다가 내 코드가 파이썬스럽게 잘 짠 거 같아서 남겨둠.
