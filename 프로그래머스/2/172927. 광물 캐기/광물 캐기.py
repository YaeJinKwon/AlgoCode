def solution(picks, minerals):
    
    n = sum(picks)
    w = dict()
    w['diamond'] = 25
    w['iron'] = 5
    w['stone'] = 1
    
    arr = []
    
    for i in range(n):
        if(len(minerals) < i*5+5):
            t = []
            for m in minerals[i*5:]:
                t.append(w[m])
            arr.append((sum(t),t))
            break
        else:
            t = []
            for m in minerals[i*5:i*5+5]:
                t.append(w[m])
            arr.append((sum(t),t))
        
    arr.sort(reverse = True)
    print(arr)
    answer = 0
    for i in range(len(arr)):
        if picks[0] > 0:
            answer+= len(arr[i][1])
            picks[0] -= 1
        elif picks[1] > 0:
            for m in arr[i][1]:
                if m == 25:
                    answer += 5
                else:
                    answer += 1
            picks[1] -=1
        else:
            if(picks[2] <=0):
                break
            for m in arr[i][1]:
                if m == 25:
                    answer += 25
                elif m == 5:
                    answer += 5
                else:
                    answer +=1
            picks[2] -= 1
            

    return answer