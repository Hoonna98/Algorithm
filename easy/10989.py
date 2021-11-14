import sys
n = int(input())
b = [0]*10001
for _ in range(n):
    b[int(sys.stdin.readline())] += 1

for i in range(10001):
    if b[i] != 0:
        for _ in range(b[i]):
            print(i)