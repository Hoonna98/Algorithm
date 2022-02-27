n = int(input())
A = list(map(int,input().split()))
D = [1] * n

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[j]+1,D[i])

for i in range(n):
    for j in range(i):
        if A[i] < A[j]:
            D[i] = max(D[j]+1,D[i])

print(max(D))

# 가장 긴 바이토닉 수열 만들기
# 첫 이중 루프로 증가만 하는 수열이 해당 지점에서 최대 길이가 몇 인지 보여준다.
# 두번 째 루프에서 해당 지점부터 감소를 한다면 최대로 감소할 길이에 이 전까지 증가했던 부분의
# 값을 더해 하나의 수열이 완성된다.