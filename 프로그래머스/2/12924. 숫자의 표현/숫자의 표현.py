
def solution(n):
    if n == 1 or n==2:
        return 1
    
    arr = [0] * ((n//2) +2)
    answer = 0
    arr[1] = 1
    s = set()
    s.add(0)
    for i in range(1, (n//2)+2):
        arr[i] = arr[i-1]+i
        s.add(arr[i-1]+i)
    
    for i in arr:
        if (i-n) in (s):
            answer+=1

    return answer +1