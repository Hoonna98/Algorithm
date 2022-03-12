from copy import deepcopy
n,m = map(int,input().split())

mat = [list(map(int,input().split())) for _ in range(n)]
cctv = []
def watch(mat,x,y,dir):
    tmp = deepcopy(mat)
    if dir == 1:
        while 0<=y<n and 0<=x<m and tmp[y][x] !=6:
            tmp[y][x] = 10
            x += 1
    elif dir == 2:
        while 0<=y<n and 0<=x<m and tmp[y][x] !=6:
            tmp[y][x] = 10
            y += 1
    elif dir == 3:
        while 0<=y<n and 0<=x<m and tmp[y][x] !=6:
            tmp[y][x] = 10
            x -= 1
    else:
        while 0<=y<n and 0<=x<m and tmp[y][x] !=6:
            tmp[y][x] = 10
            y -= 1
    return tmp
            

for i in range(n):
    for j in range(m):
        if mat[i][j] != 0 and mat[i][j] != 6:
            cctv.append([j,i,mat[i][j]])

def dfs(num,mat):
    global ma 
    tmp = deepcopy(mat)
    if num == len(cctv):
        cnt = 0
        for i in mat:
            cnt += i.count(0)
        ma = min(cnt,ma)
        return 
    if cctv[num][2] == 1:
        dfs(num+1,watch(tmp,cctv[num][0],cctv[num][1],1))
        dfs(num+1,watch(tmp,cctv[num][0],cctv[num][1],2))
        dfs(num+1,watch(tmp,cctv[num][0],cctv[num][1],3))
        dfs(num+1,watch(tmp,cctv[num][0],cctv[num][1],4))
    if cctv[num][2] == 2:
        dfs(num+1,watch(watch(tmp,cctv[num][0],cctv[num][1],3),cctv[num][0],cctv[num][1],1))
        dfs(num+1,watch(watch(tmp,cctv[num][0],cctv[num][1],2),cctv[num][0],cctv[num][1],4))
    if cctv[num][2] == 3:
        dfs(num+1,watch(watch(tmp,cctv[num][0],cctv[num][1],1),cctv[num][0],cctv[num][1],2))
        dfs(num+1,watch(watch(tmp,cctv[num][0],cctv[num][1],2),cctv[num][0],cctv[num][1],3))
        dfs(num+1,watch(watch(tmp,cctv[num][0],cctv[num][1],3),cctv[num][0],cctv[num][1],4))
        dfs(num+1,watch(watch(tmp,cctv[num][0],cctv[num][1],4),cctv[num][0],cctv[num][1],1))
    if cctv[num][2] == 4:
        dfs(num+1,watch(watch(watch(tmp,cctv[num][0],cctv[num][1],1),cctv[num][0],cctv[num][1],2),cctv[num][0],cctv[num][1],3))
        dfs(num+1,watch(watch(watch(tmp,cctv[num][0],cctv[num][1],1),cctv[num][0],cctv[num][1],2),cctv[num][0],cctv[num][1],4))
        dfs(num+1,watch(watch(watch(tmp,cctv[num][0],cctv[num][1],2),cctv[num][0],cctv[num][1],3),cctv[num][0],cctv[num][1],4))
        dfs(num+1,watch(watch(watch(tmp,cctv[num][0],cctv[num][1],1),cctv[num][0],cctv[num][1],4),cctv[num][0],cctv[num][1],3))
    if cctv[num][2] == 5:
        dfs(num+1,watch(watch(watch(watch(tmp,cctv[num][0],cctv[num][1],2),cctv[num][0],cctv[num][1],1),cctv[num][0],cctv[num][1],4),cctv[num][0],cctv[num][1],3))


ma = 100
dfs(0,mat)
print(ma)


# cctv 의 종류에 따라 감시할 수 있는 범위가 있어 모든 경우에 대해 탐색해야한다.
# watch 함수를 통해 cctv가 한 방향을 바라보았을 때 볼 수 있는 곳을 10으로 바꾸어준다.
# 모든 경우로 재귀 함수를 돌려 최소 값을 구해준다.

# 더 빠르게 구현하는 법
# watch함수의 리턴 값에 몇개를 보게 되었는지 체크해준다.(결과를 들고 가서 최소값 찾기)
# 이렇게 해주게 되면 마지막 depth 에서 리스트의 모든 0을 찾는 시간을 줄일 수 있다.
# 깔끔한 코드
# 모드를 나열하는 것이 아닌 리스트로 만들어 for문을 이용하는 방식
# watch 함수 또한 i번째의 방향에 대해 정리하여 더 간결하게 표현 가능