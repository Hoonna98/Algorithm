testn = int(input())

for _ in range(testn):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    big_r = max(r1,r2)
    sml_r = min(r1,r2)
    dist = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    print(-1 if dist==0 and r1==r2 else 0 if r1+r2<dist or big_r-sml_r > dist \
        else 1 if r1+r2 ==dist or big_r-sml_r==dist else 2) 