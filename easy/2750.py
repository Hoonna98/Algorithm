n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

a = sorted(a)
for i in range(n):
    print(a[i])