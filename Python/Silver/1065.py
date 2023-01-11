n = int(input())

def hansoo(number):
    cnt = 0
    for i in range(1, n+1):
        if i < 10:
            cnt += 1
            continue
        number = [int(x) for x in str(i)]
        d = number[0] - number[1]
        diff = []

        for j in range(len(number)-1):
            diff.append(number[j] - number[j+1])

        if diff.count(d) == len(number) - 1:
            cnt += 1

    return cnt

print(hansoo(n))
