n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
while True:
    D = [0] * n
    for i in range(n):
        for j in range(n):
            if (A[i][0] > A[j][0] and A[i][1] < A[j][1]) or (A[i][0] < A[j][0] and A[i][1] > A[j][1]) :
                D[i] += 1
    if max(D) == 0:
        print(cnt)
        break
    A[D.index(max(D))] = [501,501]
    cnt += 1

# 전깃줄이 교차하는 조건이 (A[i][0] > A[j][0] and A[i][1] < A[j][1]) or (A[i][0] < A[j][0] and A[i][1] > A[j][1]) 이다
# 이 경우일 때 D[i]에 1을 더해주면 가장 많이 겹치는 줄을 찾게 된다.
# 문제의 조건이 모든 전깃줄이 교차하지 않기 위한 제거해야하는 최소 전깃줄 수이기에 가장 많이 교차하는 전깃줄부터 지워가면 답을 찾을 수 있다.
# 다른 방식의 DP로 접근하는 방법도 있으니 2565_dp 파일에서 시도해보기로 한다.