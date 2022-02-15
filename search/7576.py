from collections import deque
import sys

m,n = map(int, sys.stdin.readline().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
queue = deque()

for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            queue.append([j,i])

def bfs():
    result = 0
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            if 0 <= x+dx[i] < m and 0 <= y+dy[i] < n and farm[y+dy[i]][x+dx[i]] == 0:
                farm[y+dy[i]][x+dx[i]] = farm[y][x] + 1
                result = max(result, farm[y][x]+1)
                queue.append([x+dx[i],y+dy[i]])

    if result == 0:
        return 0
    return result - 1

result = bfs()
for i in farm:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(result)
