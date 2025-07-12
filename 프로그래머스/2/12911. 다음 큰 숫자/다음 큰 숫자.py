def solution(n):
    nBin = format(n, 'b')
    nBinOne = str(nBin).count('1')
    a = n+1
    while(True):
        aBin = format(a, 'b')
        aBinOne = str(aBin).count('1')
        if aBinOne == nBinOne:
            break      
        a +=1
    return a