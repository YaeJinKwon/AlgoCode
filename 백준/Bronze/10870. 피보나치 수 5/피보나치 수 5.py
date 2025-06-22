import sys
input = sys.stdin.readline

def fibo(i):
    if(i <= 1):
        return i                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    return fibo(i-1) + fibo(i-2)
    

n = int(input())
print(fibo(n))