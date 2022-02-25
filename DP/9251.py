import sys
input = sys.stdin.readline
a,b = input(), list(input().rstrip())
D = [0] * len(b)
k = 0

for i in range(len(a)):
    cnt = 0
    for j in range(len(b)):
        if cnt < D[j]: # 이어진 것 중 가장 마지막 값 찾는 중
            cnt = D[j]
        elif a[i] == b[j] : # 이어진 것 중 가장 마지막 이후에 같은 것이 있는 지 확인 후 더하기
            D[j] = cnt + 1
            
print(max(D))

# a에서 한글자 씩 꺼내서 B 전체와 비교 한다.
# 이어진 부분이 있다면 이어진 부분의 제일 마지막으로 이동한 후 
# 그 이후에 같은 글자가 있는지 확인한다.
# O(N**2) 시간 복잡도
