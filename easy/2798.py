n,m = map(int, input().split())
card = list(map(int, input().split()))

max = 0
while True:
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if max < card[i]+card[j]+card[k] and card[i]+card[j]+card[k] <= m :
                    max = card[i]+card[j]+card[k]
                if max == m:
                    break
    break
print(max)



    