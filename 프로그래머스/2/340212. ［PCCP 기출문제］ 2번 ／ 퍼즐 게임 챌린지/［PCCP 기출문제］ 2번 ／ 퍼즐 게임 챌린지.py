def solution(diffs, times, limit):

    start = 1
    end  = max(diffs)

    while(start <= end):
        mid = (start + end)//2
        time = 0
        for i in range(len(diffs)):
            if mid < diffs[i]:
                time+= (diffs[i] - mid)*(times[i-1]+times[i]) + times[i]
            else:
                time += times[i]
        if time ==limit:
            start = mid
            break
        elif time <limit:
            end = mid - 1
        else:
            start = mid+1
        
                   
    return start