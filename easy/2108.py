import sys
from collections import Counter
n = int(input())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a = sorted(a)

print(int(round(sum(a)/n,0)))
print(a[n//2])
b = []
b = Counter(a).most_common()
if len(b) > 1 and b[0][1] == b[1][1]:
    print(b[1][0])
else:
    print(b[0][0])
print(max(a)-min(a))