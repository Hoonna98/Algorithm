n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
a = sorted(a)
for i in range(n):
    print(a[i][0],a[i][1])