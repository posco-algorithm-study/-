n = int(input())
workers = []

for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        workers.append(name)
    elif state == 'leave':
        workers.remove(name)

workers.sort(reverse = True)
for w in workers:
    print(w)
