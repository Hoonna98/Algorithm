n,m = map(int,input().split())
y,x,d = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [0,1,0,-1],[-1,0,1,0]

def lotate(d):
    if d == 0:
        return 3
    return d - 1

def clean_able(x,y,d):
    if d == 0:
        while y > 0:
            y -= 1
            if mat[y][x] == 0:
                return True
        return False

    if d == 1:
        while x < m-1:
            x += 1
            if mat[y][x] == 0:
                return True
        return False

    if d == 2:
        while y < n-1:
            y += 1
            if mat[y][x] == 0:
                return True
        return False

    if d == 3:
        while x > 0:
            x -= 1
            if mat[y][x] == 0:
                return True
        return False

cnt = 1
mat[y][x] = 2
while True:
    b = 0
    for _ in range(4):
        d = lotate(d)
        nx,ny = x+dx[d], y+dy[d]
        if mat[ny][nx] == 0:
            cnt += 1
            x,y = nx,ny
            mat[y][x] = 2
            b = 1
            break
    if b == 0:
        if mat[y-dy[d]][x-dx[d]] != 1:
            x,y = x-dx[d],y-dy[d]
            continue
        else:
            break

print(cnt)

# 청소 가능한 영역이 몇개인지 찾는 문제이다. (일반 구현 문제)
# 문제가 제시한 대로 문제를 풀면 되는데 청소한 자리를 0 -> 2로 바꾸면서 청소를 한지 체크하였다.
# 문제에서 제시한 것이 "왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다."
# 으로 되어있는데 왼쪽 첫칸만 확인하는 오류가 있는 문제이다.
