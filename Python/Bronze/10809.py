s = list(map(str, input()))

alphabet = [i for i in range(97, 124)]
result = [-1] * 26

for a in alphabet:
    if chr(a) in s:
        result[a - 97] = s.index(chr(a))

for i in range(26):
    print(result[i], end = ' ')
