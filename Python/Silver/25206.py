total, result = 0, 0
def cal(credit, score):
    credit = int(credit[0])
    if score == 'A+':
        return credit * 4.5
    elif score == 'A0':
        return credit * 4.0
    elif score == 'B+':
        return credit * 3.5
    elif score == 'B0':
        return credit * 3.0
    elif score == 'C+':
        return credit * 2.5
    elif score == 'C0':
        return credit * 2.0
    elif score == 'D+':
        return credit * 1.5
    elif score == 'D0':
        return credit * 1.0
    elif score == 'F':
        return 0

for _ in range(20):
    subject, credit, score = input().split()
    if score == 'P':
        continue
    result += cal(credit, score)
    total += int(credit[0])
print(result / total)
