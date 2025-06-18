N = int(input())

array= []
c = 2
n = N
while(True):
    t = 1
    for i in array:
        t *= i
    if t == N:
        break
    if(n%c == 0):
        array.append(c)
        n = n//c
    else:
        c +=1

for i in array:
    print(i)
