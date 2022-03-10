n,m = map(int,input().split())

A = []
for i in range(n):
    v,c,k = map(int,input().split())
    while k > 1 :
        tmp = k - (k >> 1)
        A.append([v*tmp,c*tmp])
        k = k >> 1
    A.append([v,c])

D = [[0]*(m+1) for _ in range(len(A)+1)]
n = len(A)

def knap(i,w):
    if D[i][w] != 0:
        return D[i][w]
    if i == n:
        return 0
    
    D[i][w] = max(A[i][1] + knap(i+1,w+A[i][0]) if A[i][0]+w <= m else 0, knap(i+1,w))
    return D[i][w]

print(knap(0,0))

# knapsack문제에서 동일한 물건이 여러 개 있는 문제
# 모든 물건을 쪼개어 일반 배낭문제와 같이 풀 수 있지만 시간과 메모리초과가 일반 배낭에 비해 과도하게 많이 발생한다.
# 그래서 물건이 n개 있을 때 1부터 n개 까지 모든 조합을 만들 수 있게 물건을 쪼개주어야한다.
# 11개가 있다고 가정해보자.
# 11 - 5(11 >> 1) = 6
# 5 - 2(5 >> 1) = 3
# 2 - 1(2 >> 1) = 1
# 1 - 0(1 >> 1) = 1
# RHS(Right hand side)에 있는 값들로 조합을 이루면 1부터 11을 전부 만들 수 있게된다.
# 이렇게 물건을 저장하고 knapsack문제와 동일하게 돌리는게 최선이지만 파이썬으로 제출하게되면 시간과 메모리가 초과나서
# 파이썬으로는 풀 수 없다