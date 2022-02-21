from collections import deque

m,n,h = map(int,input().split())
farm = [list(map(int,input().split())) for _ in range(n*h)]
queue = deque()
dx, dy, dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]
for z in range(h):
    for i in range(n):
        for j in range(m):
            if farm[i+n*z][j] == 1:
                queue.append([j,i,z])

def bfs():
    res = 0
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            xx,yy,zz = x+dx[i], y+dy[i], n*(z+dz[i])
            if 0 <= xx < m and 0 <= yy < n and 0 <= z+dz[i] < h and farm[yy+zz][xx] == 0:
                farm[yy+zz][xx] = farm[y+(n*z)][x] + 1
                queue.append([xx,yy,z+dz[i]])
                res = max(res, farm[yy+zz][xx])
    
    if res == 0:
        return 0
    return res - 1

result = bfs()
for i in farm:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(result)