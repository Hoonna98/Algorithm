from collections import deque
from copy import deepcopy
from itertools import combinations
n,m = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
home, chk = [],[]
dx,dy = [1,-1,0,0],[0,0,1,-1]
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            home.append([j,i,0])
        elif mat[i][j] == 2:
            mat[i][j] = 0
            chk.append([j,i])

def bfs(mat2):
    al = 0
    for item in home:
        que = deque()
        que.append(item)
        visited = [[False]*n for _ in range(n)]
        while que:
            x,y,cnt = que.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and mat2[ny][nx] != 1:
                    if mat2[ny][nx] == 2:
                        al += cnt+1
                        que.clear()
                        break
                    visited[ny][nx] = True
                    que.append([nx,ny,cnt+1])
    return al
mi = float('inf')
for item in combinations(chk,m):
    tmp = deepcopy(mat)
    for a in item:
        tmp[a[1]][a[0]] = 2
    mi = min(mi,bfs(tmp))

print(mi)

# 치킨 배달 문제
# 치킨 집의 개수를 M개로 줄였을 때 집에서 치킨집까지 모든 거리의 합이 최소가 되는
# 치킨 집의 위치를 구하는 것이다.
# 치킨 집의 위치는 조합을 이용하여 모든 경우의 수를 다 구하였고
# 해당 치킨 집까지의 거리는 bfs를 이용하여 모든 집집마다 거리를 확장해나가 
# 치킨 집을 찾으면 바로 거리를 리턴하는 방식을 이용하였다.
# bfs로 코드를 구현하게 되면 치킨집까지의 거리를 구하는 시간이 너무 오래 걸렸고,
# 중간에 장애물이 없기에 둘 사이의 거리를 bfs로 이용하지 않는 것이 효과적이다.