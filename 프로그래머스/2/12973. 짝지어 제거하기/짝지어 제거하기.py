def solution(s):
    answer = -1
    sL = []
    sL.append(s[0])
    for i in range(1, len(s)):
        if len(sL) == 0:
            sL.append(s[i])
            continue
        if sL[-1] == s[i]:
            sL.pop()
        else:
            sL.append(s[i])
    if(len(sL)>0):
        return 0
    
    return 1