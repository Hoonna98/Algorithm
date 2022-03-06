n,m,y,x,_ = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
dice = [0] * 6
dx,dy = [0,1,-1,0,0],[0,0,0,-1,1]
k = list(map(int,input().split()))

def roll(direc):
    if direc == 1:
        dice[1],dice[4],dice[3],dice[5] = dice[4],dice[3],dice[5],dice[1]
    elif direc == 2:
        dice[5],dice[3],dice[4],dice[1] = dice[3],dice[4],dice[1],dice[5]
    elif direc == 3:
        dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
    else:
        dice[3],dice[2],dice[1],dice[0] = dice[2],dice[1],dice[0],dice[3]

for act in k:
    nx, ny = x + dx[act], y + dy[act]
    if 0 <= nx < m and 0 <= ny < n:
        x,y = nx,ny
        roll(act)
        if mat[ny][nx] == 0:
            mat[ny][nx] = dice[1]
        else:
            dice[1] = mat[ny][nx]
            mat[ny][nx] = 0
        print(dice[3])

# 주사위 굴리기 문제
# 주사위가 굴러가는 것만 잘 구현하면 문제 없이 풀 수 있다.
# 주의해야할 것은 판의 좌표가 (y,x)로 들어와서 이 부분만 주의하면 문제없이 풀 수 있다.
# 주사위의 윗부분을 index 3에, 1을 바닥에 고정하고 구를 때 마다 값을 바꾸어주었다.

# 한 번에 대입 하는 방식으로 코드의 길이를 줄이고, tmp변수를 사용하지 않아도 구현할 수 있다.
# tmp = dice[1]
# dice[1] = dice[4]
# dice[4] = dice[3]
# dice[3] = dice[5]
# dice[5] = tmp

# 파이토닉한 코드
# dice[1],dice[4],dice[3],dice[5] = dice[4],dice[3],dice[5],dice[1]