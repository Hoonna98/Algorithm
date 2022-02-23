D = [[[0]*21 for _ in range(21)] for _ in range(21)]
D[0][0][0] = 1
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        a = b = c = 0
    if a > 20 or b > 20 or c > 20:
        a = b = c = 20
    if D[a][b][c] != 0:
        return D[a][b][c]
    if a < b < c:
        D[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        D[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return D[a][b][c]


while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a,b,c,w(a,b,c)))
    