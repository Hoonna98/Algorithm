from collections import deque
from copy import deepcopy
n ,m = map(int, input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
start = []
empty = []
dx, dy = [1,-1,0,0],[0,0,1,-1]

for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            start.append([j,i])
        if mat[i][j] == 0:
            empty.append([j,i])
lenm = len(empty)

cnt = 0


def bfs(bod):
    que = deque(start)
    cn = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n and bod[ny][nx] == 0:
                bod[ny][nx] = 2
                cn += 1
                que.append([nx,ny])
    return cn

for i in range(lenm):
    for j in range(i+1,lenm):
        for k in range(j+1, lenm):
            tmpm = deepcopy(mat)
            tmpm[empty[i][1]][empty[i][0]] = 1
            tmpm[empty[j][1]][empty[j][0]] = 1
            tmpm[empty[k][1]][empty[k][0]] = 1
            cnt = max(lenm-3-bfs(tmpm),cnt)


print(cnt)
