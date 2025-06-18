

a, b, c = map(int,input().split())
if(max(a,b,c)>=a+b+c - max(a,b,c)):
    s = a+b+c - max(a,b,c) 
    print(2*s-1)
else:
    print(a+b+c)
