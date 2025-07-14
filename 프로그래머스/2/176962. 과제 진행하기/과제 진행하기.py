

def solution(plans):
    answer = []

    plans.sort(key = lambda x : x[1])

    stop  = []
    
    for i in range(len(plans)-1):
        time = int(plans[i][1][:2])*60 + int(plans[i][1][3:])
        nextTime= int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:])
        
        if (time + int(plans[i][2])) > nextTime:
            stop.append((plans[i][0], 
                       int(plans[i][2]) - (nextTime - time)))
        elif (time + int(plans[i][2])) == nextTime :
            answer.append(plans[i][0])
        else:
            answer.append(plans[i][0])
            left = nextTime - time - int(plans[i][2])
            while (left>0 and len(stop) >0) :
                if (stop[-1][1] <= (left)):
                    t = stop.pop()
                    answer.append(t[0])
                    left -= t[1]
                else :
                    stop[-1] = (stop[-1][0], stop[-1][1] - left)
                    left = 0
                    break

    answer.append(plans[-1][0])
    
    while stop:
        answer.append(stop.pop()[0])
    return answer