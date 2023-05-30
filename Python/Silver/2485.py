# 2485 가로수
"""
5.30.화.2023
idea : 가로등 간의 간격(diff)의 GCD가 새 가로수 간의 간격
"""
import sys
import math
input = sys.stdin.readline

n = int(input())
pos = []
for _ in range(n):
    pos.append(int(input()))

diff = []
for i in range(1, n):
    diff.append(pos[i] - pos[i-1])

gcd = math.gcd(*diff) # 새 가로수 간의 간격

cnt = (pos[-1] - pos[0]) // gcd - n + 1
print(cnt)
