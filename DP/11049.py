n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
x = A[0][0]
D = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        D[i][j] = D[i][j-1] + A[i][0] * A[j][0] * A[j][1]


for i in range(n):
    for j in range(i+1,n):
        for k in range(i,j):
            D[i][j] = min(D[i][j],D[i][k]+D[k+1][j]+A[i][0] * A[k][1] * A[j][1])
print(D[0][n-1])