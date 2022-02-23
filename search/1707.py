import sys

k = int(sys.stdin.readline().rstrip())

def check(r,l, edge):    
    for item in edge:
        if (item[0] in r and item[1] in r) or (item[0] in l and item[1] in l):
            return False
    for it in r:
        pas = False
        for item in edge:
            if it in item:
                pas = True
                continue
        if not pas:
            return False
    for it in l:
        pas = False
        for item in edge:
            if it in item:
                pas = True
                continue
        if not pas:
            return False
    return True

for _ in range(k):
    numv, nume = map(int, sys.stdin.readline().rstrip().split())
    edge = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(nume)]
    r, l, all = set(), set(), set([i for i in range(1,numv+1)])

    for item in edge:
        if item[0] == 1:
            l.add(item[1])
        if item[1] == 1:
            l.add(item[0])
    r = all - l
    if check(r,l,edge):
        print("YES")
    else:
        print("NO")
