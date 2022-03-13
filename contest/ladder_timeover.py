from copy import deepcopy
from collections import deque
n,m,h = map(int,input().split())

ma = [list(map(int,input().split())) for _ in range(m)]
ma.sort()
su = 0
able = []
def succues(ma):
    for i in range(1,n+1):
        cur = i
        for row in ma:
            if row[1] == cur:
                cur += 1
            elif row[1] == cur-1:
                cur -= 1
        if cur != i:
            return False
    return True

def find_albe(ma):
    for b in range(1,n):
        for a in range(1,h+1):
            if add_able(ma,a,b):
                able.append([a,b])
    return able

add_able = lambda ma,a,b : False if [a,b] in ma or [a,b-1] in ma else True
able = find_albe(ma)
def bfs(ma,depth=0):
    que = deque()
    que.append([ma,0])
    if succues(ma):
        return depth
    while que:
        m2 = que.popleft()
        if m2[1] == 4:
            return -1
        for item in able:
            tmp2 = deepcopy(m2[0])
            if add_able(tmp2,item[0],item[1]):
                tmp2.append(item)
                tmp2.sort()
                if succues(tmp2):
                    return m2[1]+1
                que.append([tmp2,m2[1]+1])
    return -1

print(bfs(ma))

# 사다리 조작 문제
# 어떤 상황에서 사다리를 탓을 때 사다리의 수행결과를 리턴해주는 함수를 만들었고,
# depth를 늘려나가면서 현재 상태를 저장하고 넘겨주었다.
# sort를 통해 맨 위에서부터 현재 상태에서 탈 수 있는 사다리를 찾아나갔는데
# 수가 많아질 수 록 소트가 많아져 시간이 너무 많이 걸리게 되어 시간초과가 났다.

# 다음에 다시 풀어볼 예정