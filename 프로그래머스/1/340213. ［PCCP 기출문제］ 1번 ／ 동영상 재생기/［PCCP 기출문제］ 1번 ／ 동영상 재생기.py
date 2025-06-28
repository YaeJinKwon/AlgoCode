def solution(video_len, pos, op_start, op_end, commands):    

    nvideo_len = int(video_len[:2])*60 + int(video_len[3:])
    npos = int(pos[:2]) *60 + int(pos[3:])
    nop_start = int(op_start[:2]) *60 + int(op_start[3:])
    nop_end = int(op_end[:2]) *60 + int(op_end[3:])
    
    
    for command in commands:
        if nop_start <= npos < nop_end:
            npos = nop_end
        if command == "next":
            if npos+10 > nvideo_len:
                npos = nvideo_len
            else:
                npos +=10
        elif command == "prev":
            if npos - 10 < 0:
                npos = 0
            else:
                npos -=10
                
    if nop_start <= npos < nop_end:
        npos = nop_end
    ans = []

    if npos//60 <10:
        ans.append('0')
    ans.append(str(npos//60))
    ans.append(':')
    if npos%60 <10:
        ans.append('0')
    ans.append(str(npos%60))
        
    answer = "".join(ans)
            
            
                
                
                
        
        


            
    return answer