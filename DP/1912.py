import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
D = [-1001] * n

for i in range(n):
    if D[i-1]+A[i] > A[i]:
        D[i] = D[i-1]+A[i]
    else:
        D[i] = A[i]

print(max(D))

# 연속합이 가장 큰 값을 찾는 문제
# 이전 값 + 현재 값이 현재값 보다 크면 저장하면 끝이다.