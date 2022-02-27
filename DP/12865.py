n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
D = [[0]* (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w = A[i-1][0]
    v = A[i-1][1]
    for j in range(1,k+1):
        if j < w:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j], D[i-1][j-w]+v)
        

print(D[n][k])