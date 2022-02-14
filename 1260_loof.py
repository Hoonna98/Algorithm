from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end = " ")

    for i in range(n+1):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(i)

def bfs_loop(v):
    queue = deque()
    queue.append(v)
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for i in range(n+1):
            if graph[v][i] == 1 and visited[i] == True:
                queue.append(i)
                visited[i] = False
                

n,m,v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


dfs(v)
print()
bfs_loop(v)