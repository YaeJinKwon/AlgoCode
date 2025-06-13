def solution(s):
    
    length = len(s)
    result = length
    for i in range(1, length+1):
        answer = length
        count = 0
        for j in range(0, length, i):
            if(s[j:j+i] == s[j+i:j+(i*2)]):
                count+=1
            else:
                if(count>0):
                    num = str(count+1)
                    answer = (answer - (i*(count+1))) + i + len(num)
                    count = 0
        result = min(answer, result)
        
        
    return result