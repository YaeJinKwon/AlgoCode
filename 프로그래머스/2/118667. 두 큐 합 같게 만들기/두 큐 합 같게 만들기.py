from collections import deque

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    tempQ1 =deque(queue1)
    tempQ2 =deque(queue2)
    limit = (len(queue1))*3
    sum1 = sum(tempQ1)
    sum2 = sum(tempQ2)
    answer = -1
    count = 0
    while(len(tempQ1)>0 or len(tempQ2) >0):
        if count>limit:
            break
        if (sum1 == sum2 ):
            break
        elif(sum1 < total//2):
            a = tempQ2.popleft()
            tempQ1.append(a)
            sum1 += a
            sum2 -= a
        else:
            a = tempQ1.popleft()
            tempQ2.append(a)
            sum1 -= a
            sum2 += a

        
        count+=1

    
    if (sum(tempQ1) == total//2):
        answer = count

    return answer