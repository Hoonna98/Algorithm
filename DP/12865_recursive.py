n,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
D = [[0]*(k+1) for _ in range(n+1)]

def knap(i,w):
    if D[i][w] != 0:
        return D[i][w]
    if i == n:
        return 0

    D[i][w] = max(0 if a[i][0] + w > k else a[i][1] + knap(i+1,w+a[i][0]) ,knap(i+1,w))
    return D[i][w]

print(knap(0,0))

# 가장 대표적인 knapsack 문제
# i번째의 물건을 선택했을 때와 선택하지 않았을 때 두 경우에 대해
# 모든 아이템을 담고 빼보면 된다.
# 재귀로 아이템을 선택한 경우와 선택하지 않은 모든 경우를 찾으면된다.
# 속도 증가로 이미 찾은 결과에 대해 값을 저장해놓게되면 DP의 문제가 된다.