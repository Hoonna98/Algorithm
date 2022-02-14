from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=" ")

    for item in graph:
        if item[0] == v and visited[item[1]] == False:
            dfs(item[1])
        if item[1] == v and visited[item[0]] == False:
            dfs(item[0])
    
def bfs_recursive(v):
    visited[v] = False
    print(v, end=" ")
    for item in graph:
        if item[0] == v and visited[item[1]] == True:
            queue.append(item[1])
            visited[item[1]] = False
            
        if item[1] == v and visited[item[0]] == True:
            queue.append(item[0])
            visited[item[0]] = False
        
    if len(queue) > 0 : bfs_recursive(queue.popleft()), 0


n,m,v = map(int, input().split())
visited = [False] * (n + 1)

graph = []
for _ in range(m):
    graph.append(list(map(int,input().split())))
graph = sorted(graph, key = lambda x:x[1])
queue = deque()

dfs(v)
print()
bfs_recursive(v)