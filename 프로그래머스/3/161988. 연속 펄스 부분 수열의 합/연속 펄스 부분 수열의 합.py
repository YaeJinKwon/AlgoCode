def solution(sequence):
    
    answer = -1e9
    first = []
    for i in range(len(sequence)):
        if i % 2 == 0:
            first.append(sequence[i])
        else:
            first.append(-1 * sequence[i])
                 
    min1 = 0
    total = 0
    for i in range(len(first)):
        total += first[i]
        min1 = min(total, min1)
        answer = max(total - min1, answer)
                
        
        
        
    second = []
    for i in range(len(sequence)):
        if i % 2 == 0:
            second.append(-1*sequence[i])
        else:
            second.append(sequence[i])
              
    min2 = 0
    total = 0
    for i in range(len(second)):
        total += second[i]
        min2 = min(total, min2)
        answer = max(total - min2, answer)
                   
            

    return answer