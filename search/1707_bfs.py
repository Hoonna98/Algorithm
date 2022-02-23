from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    que = deque()
    que.append(v)
    while que:
        c = que.popleft()
        for item in edge:
            if item[0] == c:
                if dis[item[1]] == 0:
                    dis[item[1]] = dis[c]+1
                    que.append(item[1])
                elif dis[item[1]] == dis[c]:
                    return 0
            if item[1] == c:
                if dis[item[0]] == 0:
                    dis[item[0]] = dis[c]+1
                    que.append(item[1])
                elif dis[item[0]] == dis[c]:
                    return 0

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    nv,ne = map(int, input().split())
    dis = [0]*(nv+1)
    edge = [list(map(int, input().split())) for _ in range(ne)]
    
    for i in range(1,nv+1):
        if dis[i] == 0:
            if bfs(i) == 0:
                print("NO")
                break
    if i == nv:
        print("YES")

    