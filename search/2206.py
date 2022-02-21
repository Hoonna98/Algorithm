from collections import deque
import sys
n, m = map(int,sys.stdin.readline().split())

mat = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
dx,dy = [1,0,0,-1],[0,1,-1,0]

def bfs():
    que = deque()
    que.append([0,0,0,False])
    if [n,m] == [1,1]:
        return 1
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True

    while que:
        x, y, c, block = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if [nx, ny] == [m-1,n-1]:
                return c + 2
            if block == False and 0<=nx<m and 0<=ny<n and mat[ny][nx] == 1:
                visited[ny][nx][1] = True
                que.append([nx,ny,c+1,True])
            if block:
                if 0<=nx<m and 0<=ny<n and visited[ny][nx][1] == False and mat[ny][nx] != 1:
                    visited[ny][nx][1] = True
                    que.append([nx,ny,c+1,block])
            else:
                if 0<=nx<m and 0<=ny<n and visited[ny][nx][0] == False and mat[ny][nx] != 1:
                    visited[ny][nx][0] = True
                    que.append([nx,ny,c+1,block])
                   
    return -1

print(bfs())