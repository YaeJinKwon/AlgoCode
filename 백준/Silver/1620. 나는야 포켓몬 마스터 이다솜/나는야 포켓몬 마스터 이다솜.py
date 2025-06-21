import sys

input = sys.stdin.readline

n, m = map(int,input().split())

da = dict()
dn = dict()
for i in range(1,n+1):
    po = input().rstrip()
    dn[i] = po
    da[po] = i
for _ in range(m):
    s = input().rstrip()
    if(s.isnumeric()):
        print(dn[int(s)])
    else:
        print(da[s])
