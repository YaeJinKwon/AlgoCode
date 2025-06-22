import sys
input = sys.stdin.readline

def facto (i):
    if(i <= 1):
        return 1
    return i * facto(i-1)


n = int(input())
print(facto(n))