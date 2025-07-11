def solution(s):
    arr = []
    s = s.lower()
    if len(s)==1:
        return s.upper()
    arr.append(s[0].upper())
    for i in range(len(s)-1):
        if s[i] == ' ':
            arr.append(s[i+1].upper())
        else:
            arr.append(s[i+1])
            
            
    
    return ''.join(arr)