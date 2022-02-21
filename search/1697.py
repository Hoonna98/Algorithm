from collections import deque
n, k = map(int,input().split())

nx = [2,-1,1]
mat = [0]*100001

def bfs():
    que = deque()
    que.append([n,0])
    mat[n] = 1

    if n == k:
        return 0

    while que:
        x,c = que.popleft()
        for i in range(3):
            if i == 0:
                nn = x
            else:
                nn = nx[i]
            if 0 <= x+nn <= 100000 and mat[x+nn] == 0:
                que.append([x+nn,c+1])
                mat[x+nn] = 1
                if x+nn == k:
                    return c + 1
print(bfs())
