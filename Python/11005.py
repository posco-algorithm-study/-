# 11005
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split()) # n을 b진법으로, b최대 36
ans = ''

while n != 0:
    ans += str(tmp[n % b])
    n //= b
    
print(ans[::-1])
