words = list(input())
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 1
for i in range(1, len(words)):
    if words[i] == '-' or words[i] == '=':
        if words[i-1] == 'z' and words[i-2] == 'd':
            cnt -= 1
        continue
    elif words[i] == 'j' and (words[i-1] == 'l' or words[i-1] == 'n'):
        pass
    else:
        cnt += 1

print(cnt)
