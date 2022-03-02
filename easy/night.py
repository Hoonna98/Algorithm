loc_ = ['a','b','c','d','e','f','g','h']
loc = input()
x = loc_.index(loc[0])
y = int(loc[1])-1
dx,dy = [2,-2,2,-2,1,-1,1,-1], [1,-1,-1,1,2,-2,-2,2]
cnt = 0
T = lambda a, da, b, db : 0 <= a+da < 8 and 0 <= b+db < 8
for i in range(8):
    if T(x,dx[i],y,dy[i]):
        cnt += 1
print(cnt)