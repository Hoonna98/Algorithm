n = int(input())
cnt = 0
drg = [list(map(int,input().split())) for _ in range(n)]
map = [[0]*101 for _ in range(101)]
dx,dy = [1,0,-1,0],[0,-1,0,1]
lotate = lambda d : (d+1)%4
for item in drg:
    x,y,d,g = item
    map[y][x] = 1
    map[y+dy[d]][x+dx[d]] = 1
    fx,fy = x+dx[d],y+dy[d]
    dirc = [d]
    for _ in range(g):
        lend = len(dirc)
        for i in range(lend-1,-1,-1):
            dd = lotate(dirc[i])
            dirc.append(dd)
            fx,fy = fx+dx[dd],fy+dy[dd]
            map[fy][fx] = 1

for i in range(100):
    for j in range(100):
        if map[i][j] == 1 and map[i+1][j] == 1 and map[i][j+1] and map[i+1][j+1]:
            cnt+=1

print(cnt)

# 드래곤 커브 문제
# 일반적인 구현 문제
# 드래곤 커브가 세대가 늘어날 수록 회전을 하게되는데 회전을 해서 어떻게 결과가 나는지만 찾으면 된다.
# 이 커브는 회전을 할 때 해당 모양에서 90도가 움직이게 되는데
# 표현하기위해서 돌기 전 모양의 끝 점에서 이전 지점으로 이동해가며 방향을 저장하고 해당 방향을 90도씩 회전해서 
# 그 방향으로 끝 점을 계속 이동해나가면 된다.