n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

min_ = 64
for i in range(n-7):
    for j in range(m-7):
        startw=0
        startb=0
        for x in range(8):
            for y in range(8):
                if (x+y)%2 == 0:
                    if board[i+x][j+y] == 'W': startb += 1
                    else: startw += 1
                else:
                    if board[i+x][j+y] == 'B': startb += 1
                    else: startw += 1
        if min_ > min(startw,startb):
            min_ = min(startw,startb)
print(min_)
