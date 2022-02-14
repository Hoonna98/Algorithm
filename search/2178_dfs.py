n,m = map(int, input().split())
miro = []
for i in range(1,n+1):
    miro.append(list(input()))

inner = lambda x, y, dx, dy : x+dx in range(n) and y+dy in range(m)
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0
result = 10000

def dfs(x,y):
    global cnt, result
    stack = []
    cnt += 1
    miro[x][y] = '0'
    stack.append([x,y])

    if (x == n-1 and y == m-1):
        miro[x][y] = '1'
        if cnt < result:
            result = cnt
            cnt -= 1
            return

    for i in range(4):
        if inner(x,y,dx[i],dy[i]) and miro[x+dx[i]][y+dy[i]] == '1':
            dfs(x+dx[i],y+dy[i])
            
    miro[x][y] = '1'
    x,y = stack.pop()
    cnt -= 1

dfs(0,0)
print(result)

        

