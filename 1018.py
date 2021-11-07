n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

min = 64
for i in range(n-7):
    for j in range(m-7):
        count = 0
        for k in range(1,64):
            if (i+int(k/8)+j+k%8) % 2 == 0:
                if board[i][j] != board[i+int(k/8)][j+k%8]:
                    count += 1
            else:
                if board[i][j] == board[i+int(k/8)][j+k%8]:
                    count += 1
        if count < min:
            min = count
            print(i, j)
        count = 1
        for k in range(1,64):
            if (i+int(k/8)+j+k%8) % 2 == 0:
                if board[i][j] == board[i+int(k/8)][j+k%8]:
                    count += 1
            else:
                if board[i][j] != board[i+int(k/8)][j+k%8]:
                    count += 1
        if count < min:
            min = count
            print(i, j, count)
print(min)

