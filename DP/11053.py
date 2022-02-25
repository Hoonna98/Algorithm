n = int(input())
A = list(map(int,input().split()))
d = [1]*(n)

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i],d[j]+1)

print(max(d))

# 가장 기본적인 DP를 이용한 LIS(Longest Increasing Subsequence)문제
# 한 칸씩 이동할 때 마다 처음부터 해당 지점까지의 가장 긴 수열의 길이를 구한다.
# O(N**2)의 시간복잡도