gear = [list(map(int,input())) for _ in range(4)]

def lotate(idx, cyc):
    if cyc == 1:
        tmp = gear[idx][7]
        for i in range(6,-1,-1):
            gear[idx][i+1] = gear[idx][i]
        gear[idx][0] = tmp
    else:
        tmp = gear[idx][0]
        for i in range(7):
            gear[idx][i] = gear[idx][i+1]
        gear[idx][7] = tmp


def check(idx,nxt,cyc):
    if nxt == 4 or nxt == -1:
        return 0

    if idx > nxt:
        if gear[nxt][2] != gear[idx][6]:
            res.append([nxt,-cyc])
            check(idx-1,nxt-1,-cyc)

    else:
        if gear[idx][2] != gear[nxt][6]:
            res.append([nxt,-cyc])
            check(idx+1,nxt+1,-cyc)


k = int(input())

for _ in range(k):
    idx,cyc = map(int,input().split())
    idx -= 1
    res = []
    res.append([idx,cyc])
    check(idx,idx+1,cyc)
    check(idx,idx-1,cyc)
    for item in res:
        lotate(item[0],item[1])

sum = 0
if gear[0][0] == 1:
    sum += 1
if gear[1][0] == 1:
    sum += 2
if gear[2][0] == 1:
    sum += 4
if gear[3][0] == 1:
    sum += 8
print(sum)

# lotate 함수는 해당 번호의 기어가 방향이 주어졌을 때 해당 방향으로 회전하는 것을 구현하였다.
# check 함수는 시작방향에서 다음방향으로 체크하고 만약 성공했을 경우에 해당 번호의 기어가
# 돌 수 있도록 res 변수에 돌아야하는 기어의 번호와 도는 방향을 같이 주었다.
# 첫 시작 점을 res 변수에 추가한 후 양쪽으로 체크하여 현재 같이 돌게되는 기어를 찾아주었다.
# 해당 기어를 전부 찾게 되면 lotate함수를 통해 모두 돌려주면 끝나게 된다.

# 돌기 전 상태를 기준으로 기어가 연쇄적으로 돌아 찾자말자 돌리진 못하였다.
