from collections import deque
n = int(input())
apple = [list(map(int,input().split())) for _ in range(int(input()))]
lot = [list(input().split()) for _ in range(int(input()))]
dx,dy = [1,-1,0,0],[0,0,1,-1]

que = deque()
cur = [1,1]
count = 0
cur_dir = 2

def lotate(cur, dir):
    if cur == 0:
        if dir == "L":
            cur = 2
        else:
            cur = 3
    elif cur == 1:
        if dir == "L":
            cur = 3
        else:
            cur = 2
    elif cur == 2:
        if dir == "L":
            cur = 1
        else:
            cur = 0
    else:
        if dir == "L":
            cur = 0
        else:
            cur = 1
    return cur        

while True:
    for item in lot:
        if count == int(item[0]):
            cur_dir = lotate(cur_dir,item[1])
    que.append(cur)
    cur = [cur[0]+dx[cur_dir],cur[1]+dy[cur_dir]]
    count += 1
    if not (1<=cur[0]<=n and 1<=cur[1]<=n) or cur in que:
        print(count)
        break
    if cur not in apple:
        que.popleft()
    else:
        apple.remove([cur[0],cur[1]])
    

