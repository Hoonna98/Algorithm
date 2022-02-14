from collections import deque
n = int(input())

house_map = [[0]*(n+1) for _ in range(n+1)]
visited = [[False] * (n+1) for _ in range(n+1)]

for i in range(n):
    temp = input()
    for j in range(n):
        house_map[i+1][j+1] = temp[j]
    
def bfs(x,y):
    queue.append([x,y])
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            if inner(x,y,dx[i],dy[i]) and visited[x+dx[i]][y+dy[i]] == False and house_map[x+dx[i]][y+dy[i]] == '1':
                queue.append([x+dx[i],y+dy[i]])
                visited[x+dx[i]][y+dy[i]] = True
                count += 1
    return count
    
inner = lambda x, y, dx, dy : x+dx in range(1,n+1) and y+dy in range(1,n+1)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque()
result = []

for i in range(1, n+1):
    for j in range(1, n+1):
        if visited[i][j] == False and house_map[i][j] == '1':
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in result:
    print(i)

