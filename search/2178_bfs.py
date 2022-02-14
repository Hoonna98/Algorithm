from collections import deque
n,m = map(int, input().split())
miro = []
for i in range(1,n+1):
    miro.append(list(input()))

inner = lambda x, y, dx, dy : x+dx in range(n) and y+dy in range(m)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    queue = deque()
    queue.append([0,0])
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            if inner(x,y,dx[i],dy[i]) and miro[x+dx[i]][y+dy[i]] == '1':
                queue.append([x+dx[i], y+dy[i]])
                miro[x+dx[i]][y+dy[i]] = int(miro[x][y])+1
    
    return miro[n-1][m-1]

print(bfs())