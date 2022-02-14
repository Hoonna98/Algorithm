# 2667과 같은 문제
from collections import deque

inner = lambda x,y,dx,dy : x+dx in range(0,m) and y+dy in range(0,n)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        x, y = queue.popleft()
        space[x][y] = 0

        for i in range(4):
            if inner(x,y,dx[i],dy[i]) and space[x+dx[i]][y+dy[i]] == 1:
                queue.append([x+dx[i],y+dy[i]])
                space[x+dx[i]][y+dy[i]] = 0


n = int(input())
for _ in range(n):
    swam = 0
    m,n,k = map(int, input().split())
    space = [[0]*(n) for _ in range(m)]
    
    for _ in range(k):
        x,y = map(int,input().split())
        space[x][y] = 1
    for x in range(0,m):
        for y in range(0,n):
            if space[x][y] == 1:
                bfs(x,y)
                swam += 1
    
    print(swam)
            

