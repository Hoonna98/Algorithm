from copy import deepcopy
n = int(input())
inboard = [list(map(int,input().split())) for _ in range(n)]
mm = 0
dx, dy = [1,-1,0,0],[0,0,1,-1]

def union(inboard,direc):
    board = deepcopy(inboard)
    global mm
    if 0<=direc<=1:
        for y in range(n):
            if direc == 0:
                for x in range(n-1,0,-1):
                    nx = x-dx[direc]
                    if board[y][x] == 0:
                        while 0<= nx < n:
                            if board[y][nx] != 0:    
                                board[y][x] = board[y][nx]
                                board[y][nx] = 0
                                break
                            nx = nx-dx[direc]        
                    while 0<= nx < n:
                        if board[y][x] == board[y][nx]:
                            board[y][x] *= 2
                            board[y][nx] = 0
                            break
                        if board[y][x] != board[y][nx] and board[y][nx] != 0:
                            break
                        nx = nx-dx[direc]
            else:
                for x in range(n):
                    nx = x-dx[direc]
                    if board[y][x] == 0:
                        while 0<= nx < n:
                            if board[y][nx] != 0:    
                                board[y][x] = board[y][nx]
                                board[y][nx] = 0
                                break
                            nx = nx-dx[direc]        

                    while 0<= nx < n:
                        if board[y][x] == board[y][nx]:
                            board[y][x] *= 2
                            board[y][nx] = 0
                            break
                        if board[y][x] != board[y][nx] and board[y][nx] != 0:
                            break
                        nx = nx-dx[direc]

    else:
        for x in range(n):
            if direc == 2:
                for y in range(n-1,0,-1):
                    ny = y - dy[direc]
                    if board[y][x] == 0:
                        while 0<= ny < n:
                            if board[ny][x] != 0:    
                                board[y][x] = board[ny][x]
                                board[ny][x] = 0
                                break
                            ny = ny-dy[direc]        
                
                    while 0<= ny < n:
                        if board[y][x] == board[ny][x]:
                            board[y][x] *= 2
                            board[ny][x] = 0
                            break
                        if board[y][x] != board[ny][x] and board[ny][x] != 0:
                            break
                        ny = ny-dy[direc]

            else:
                for y in range(n):
                    ny = y-dy[direc]
                    if board[y][x] == 0:

                        while 0<= ny < n:
                            if board[ny][x] != 0:    
                                board[y][x] = board[ny][x]
                                board[ny][x] = 0
                                break
                            ny = ny-dy[direc]        
                    while 0<= ny < n:
                        if board[y][x] == board[ny][x]:
                            board[y][x] *= 2
                            board[ny][x] = 0
                            break
                        if board[y][x] != board[ny][x] and board[ny][x] != 0:
                            break
                        ny = ny-dy[direc]

    for i in range(n):
        mm = max(mm,max(board[i]))

    return board

def dfs(bod,cycle):
    if cycle == 0:
        return
    for i in range(4):
        dfs(union(bod,i),cycle-1)
        
dfs(inboard,5)
print(mm)

# 총 5번 움직였을 때 가장 큰 값을 찾는 것이다.
# 움직임마다 모든 판이 계속 바뀌기 때문에 움직임 4번(위,아래,오른쪽,왼쪽) 전부 5번 수행해야한다.
# 즉 4^5번의 움직임을 중첩적으로 수행
# 움직이는 부분을 dfs로 표현
# 움직임은 현재 보드를 기준으로 방향을 주어 해당 방향으로 이동했을 때를 표현한다.
# 움직임 방식 : 움직임 방향을 기준으로 움직임의 마지막 지점부터 시작하여 하나 씩 확인
# 현재 위치가 0 이면 해당 지점에서 가장 가까운 곳의 값을 현재 위치로 들고오고
# 현재 위치가 값이 있다면 0이 아닌 곳 중 가장 가까운 곳이 현재 위치랑 값이 같다면 합치는 작업을 수행한다.
# python에서 배열은 메모리의 주소를 대입하는 것으로 일반적으로 복사하게되면
# 메모리 내부의 값을 변경했을 때 모든 변수의 배열 내부 값이 변하게 되기에
# python copy 라이브러리에서 제공하는 deepcopy를 이용하여 복사한다.
# --> 메모리 내부의 값 전부를 새로운 메모리에 복사