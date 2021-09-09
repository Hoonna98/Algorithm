x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 - x2 == 0 : 
    print(x3, end = " ")
elif x1 - x3 == 0:
    print(x2, end = " ")
else:
    print(x1, end = " ")

if y1 - y2 == 0 : 
    print(y3)
elif y1 - y3 == 0:
    print(y2)
else:
    print(y1)

    