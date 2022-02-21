from collections import deque

n = int(input())

dx,dy = [0,-1,1,0],[-1,0,0,1]
matrix = [list(map(int, input().split())) for _ in range(n)]
que = deque()
who = []
able = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            que.append([j,i,0])
            matrix[i][j] = 0

def eatwho(size):
    who.clear()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < size and matrix[i][j] != 0:
                who.append([j,i])
                
    if len(who) == 0:
        return 0
    return 1

def bfs():
    size = 2
    eat = 0
    count = 0
    
    while eatwho(size):    
        visited = [[False]*n for _ in range(n)]
        while que:
            x,y,c = que.popleft()
            visited[y][x] = True
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0<= ny< n and size >= matrix[ny][nx] and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    que.append([nx,ny,c+1])
                    if [nx,ny] in who:
                        able.append([c+1,ny,nx])
                    
        if len(able) > 0:
            able.sort()
            c, y, x = able[0]
            able.clear()
        else:
            return count
        que.append([x,y,0])
        matrix[y][x] = 0
        count += c
        eat += 1
        if eat == size:
            size += 1
            eat = 0

    return count

print(bfs())
