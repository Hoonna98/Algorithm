n,m = map(int,input().split())
x,y,d = list(map(int,input().split()))
dx,dy = [0,1,0,-1],[-1,0,1,0]
mat =[list(map(int,input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
visited[y][x] = True
cnt = 1

def loat(d):
    if d == 0:
        return 3
    return d-1
    
def game(x,y,d):
    global cnt
    for _ in range(4):
        d = loat(d)
        nx, ny = x + dx[d], y + dy[d]    
        if 0 <= nx < n and 0 <= ny < m and mat[ny][nx] == 0 and not visited[ny][nx]:
            visited[ny][nx] = True
            cnt += 1
            game(nx,ny,d)

game(x,y,d)
print(cnt)
