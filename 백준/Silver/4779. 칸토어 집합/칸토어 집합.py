import sys
input = sys.stdin.readline

n = list(map(int, sys.stdin.readlines()))


def kanto(s, r, i):
    if(i == 0):
        return
    for k in range(r+3**(i-1), r+2*3**(i-1)):
        s[k] = " "
    kanto(s, r, i-1)
    kanto(s, r+2*3**(i-1), i-1)


for i in n:
    s = ['-']*3**i
    kanto(s,0,i)
    print("".join(s))

    