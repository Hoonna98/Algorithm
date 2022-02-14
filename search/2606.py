from collections import deque,Counter
n = int(input())
m = int(input())

def bfs(v):
    queue.append(v)
    
    # visited[v] = True

    # while queue:
    #     v = queue.popleft()
    #     for i in range(n+1):
    #         if graph[v][i] == 1 and visited[i] == False:
    #             visited[i] = True
    #             queue.append(i)
    
    # return Counter(visited)

    while queue:
        v = queue.popleft()
        for i in range(n+1):
            if graph[v][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)
    
    return len(visited) -1
    
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

queue = deque()

# visited = [False] * (n+1)
# print(bfs(1)[True]-1)

visited = []
print(bfs(1))