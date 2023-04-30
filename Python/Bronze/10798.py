words = [[0] * 15 for _ in range(5)]

for i in range(5):
    w = list(input())
    
    for j in range(len(w)):
        words[i][j] = w[j]

for j in range(15):
    for i in range(5):
        if words[i][j] == 0:
            continue
        print(words[i][j], end ='')
