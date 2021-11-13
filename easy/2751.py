# merge sort algorithm
import sys
def mergesort(list_):
    if len(list_) == 1:
        return list_
    mid = len(list_)//2
    b = []

    left = mergesort(list_[:mid])
    right = mergesort(list_[mid:])
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            b.append(left[i])
            i += 1
        else:
            b.append(right[j])
            j += 1
    
    b += left[i:]
    b += right[j:]

    return b

n = int(sys.stdin.readline())
list_=[]
for _ in range(n):
    list_.append(int(sys.stdin.readline()))

list_ = mergesort(list_)

for i in range(n):
    sys.stdout.write(str(list_[i])+'\n')