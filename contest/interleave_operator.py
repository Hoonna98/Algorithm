from itertools import permutations
n = int(input())
a = list(map(int,input().split()))
opt = list(map(int,input().split()))
prod = []
result = [float('inf'),float('-inf')]
for i in range(4):
    for j in range(opt[i]):
        prod.append(i)

for item in permutations(prod):
    i = 1
    res = a[0]
    for j in item:
        if j == 0:
            res = res+a[i]
        elif j == 1:
            res = res-a[i]
        elif j == 2:
            res = res * a[i]
        else:
            res = int(res/a[i])
        i += 1
    if result[1] < res:
        result[1] = res
    if result[0] > res:
        result[0] = res

print(result[1])
print(result[0])

# 연산자가 사용 될 수 있게 여러개의 연산자를 하나 씩 쪼개어 분류
# 분류한 연산자의 모든 경우의 수 계산
# 모든 경우의 수를 대입하여 순차적으로 계산하여 최대, 최소 값 저장
# python3로는 시간초과가 나와 pypy로 제출