n = int(input())

D = [n+1]*(n+1)

for i in range(2,n+1):
    if i % 3 == 0:
        D[i] = D[int(i/3)]+1
    if i % 2 == 0:
        D[i] = min(D[int(i/2)]+1, D[i])
    D[i] = min(D[i], D[i-1]+1)

print(D[i])