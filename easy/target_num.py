from collections import deque
# numbers = [1,1,1,1,1]
# target = 3
def solution(numbers, target):
    answer = 0
    que1 = deque()
    que2 = deque()
    que1.append(numbers[0])
    que1.append(-numbers[0])
    for i in range(1,len(numbers)):
        if i % 2 == 1:
            while que1:
                tmp = que1.popleft()
                que2.append(tmp-numbers[i])
                que2.append(tmp+numbers[i])
        else:
            while que2:
                tmp = que2.popleft()
                que1.append(tmp-numbers[i])
                que1.append(tmp+numbers[i])
    answer = que1.count(target) + que2.count(target)
    print(que1,que2)
            
            
    return answer
print(solution([1,1,1,1,1],3))