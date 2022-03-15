from itertools import combinations

n,m = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
home, chk = [],[]
dx,dy = [1,-1,0,0],[0,0,1,-1]
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            home.append([j,i])
        elif mat[i][j] == 2:
            mat[i][j] = 0
            chk.append([j,i])

su = float('inf')
for item in combinations(chk,m):
    cnt = 0
    for hom in home:
        cnt += min([abs(k[0]-hom[0]) + abs(k[1]-hom[1]) for k in item])
        if su <= cnt: break
    if su > cnt: su = cnt
print(su)

# 치킨 배달 문제
# 치킨 집의 개수를 M개로 줄였을 때 집에서 치킨집까지 모든 거리의 합이 최소가 되는
# 치킨 집의 위치를 구하는 것이다.
# 치킨 집의 위치는 조합을 이용하여 모든 경우의 수를 다 구하였고
# 좌표를 이용하여 현재 지점에서 가장 가까운 치킨 집이 어디인지 구하여 리턴해주었다.