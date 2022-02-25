n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
D = [1] * n

A.sort(key=lambda x : x[0])

for i in range(n):
    for j in range(i):
        if A[i][1] > A[j][1]:
            D[i] = max(D[i], D[j]+1)

print(len(D)-max(D))

# 이차원 배열 A를 어느 기준으로 필터링을 하던 상관없이 한 쪽 기준으로 필터링을 하게되면
# 필터링 한쪽이 커질수록, 다른 한쪽이 커지면 교차하지 않는다고 정의할 수 있다.
# 즉 다른 한쪽의 배열을 LIS를 이용하면 교차하지 않는 가장 긴 값이 나오는데
# 총 길이에서 빼게되면 제거해야할 전깃줄 수를 구할 수 있다.