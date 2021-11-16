n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
a.sort(key = lambda x : (x[1],x[0]))
for i in range(n):
    print(a[i][0],a[i][1])