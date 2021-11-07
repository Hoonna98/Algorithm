n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))


for i in range(n):
    rank = 1
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            rank += 1
    print(rank, end=" ")
print()