n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
D = [0]*(n+1)

for i in range(n):
    t = a[i][0]
    v = a[i][1]
    if i + t <= n:
        D[i+t] = max(D[i+t],max(D[:i+1])+v)
print(max(D))

# N번째 날까지 얻을 수 있는 가장 큰 값을 얻는 것이 문제의 핵심이다.
# 해당값을 넣었을 때 기존 그 자리의 값과 이전까지의 
# 가장 큰 값에 해당 값을 넣은 것 중 큰 값을 선택한다.
# 가장 앞에서부터 찾으며 끝까지 갔을 때 가장 큰 값을 리턴해준다.