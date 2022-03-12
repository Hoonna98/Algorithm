from itertools import combinations
n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
dif = 1e9
num = 0
com = list(combinations(range(n), int(n/2)))
for item in com:
    if num == len(com)/2:
        break # 절반을 돌리면 나머지 값은 이미 돌린 값이기에 시간 절약
    sum = 0
    isum = 0
    idif = list({i for i in range(n)} - set(item))
    
    for i in range(len(item)):
        for j in range(i+1,len(item)):
            sum = sum + mat[item[j]][item[i]] + mat[item[i]][item[j]]
    
    for i in range(len(idif)):
        for j in range(i+1,len(idif)):
            isum = isum + mat[idif[j]][idif[i]] + mat[idif[i]][idif[j]]

    if dif > abs(sum-isum):
        dif = abs(sum-isum)
    if sum-isum == 0:
        break # 0이 가장 이상적인 값이기에 0이 나오면 바로 멈추어 시간 절약
    num += 1
print(dif)

# 팀이 될 수 있는 인원의 모든 조합을 만들어 팀 마다의 능력치 계산
# 계산할 때 상대팀도 한 번에 계산하여 조합의 절반만 수행하여도 마무리 되게 설정
# set 자료구조를 사용하여 차 집합으로 상대 팀을 한번에 파악
    