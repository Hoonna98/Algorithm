n = int(input())
a = set([])
for _ in range(n):
    a.add(input())

a = list(a)
a.sort(key=lambda x : [len(x), x])
for i in a:
    print(i)
