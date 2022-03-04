n = int(input())
ap = list(map(int,input().split()))
b, c = map(int,input().split())
cnt = n
for item in ap:
    item = item - b
    if item % c and item > 0:
        cnt = cnt + int(item / c) + 1
    elif item > 0:
        cnt = cnt + int(item/c)
print(cnt)

# 첫 감독관 b를 뺏을 때 0보다 작게 되면 아무런 작업을 하지 않아야한다.
