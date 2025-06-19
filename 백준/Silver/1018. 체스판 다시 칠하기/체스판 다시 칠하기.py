def count(i, j):
    c1 = 0
    for x in range(8):
        for y in range(8):
            if(x%2 ==0):
                if(y%2==0):
                    if ch[i+x][j+y] == 'B':
                        c1+=1
                else:
                    if ch[i+x][j+y] == 'W':
                        c1+=1
            elif(x%2 !=0):
                if(y%2==0):
                    if ch[i+x][j+y] == 'W':
                        c1+=1
                else:
                    if ch[i+x][j+y] == 'B':
                        c1+=1
    c2 =0               
    for x in range(8):
        for y in range(8):
            if(x%2 ==0):
                if(y%2==0):
                    if ch[i+x][j+y] == 'W':
                        c2+=1
                else:
                    if ch[i+x][j+y] == 'B':
                        c2+=1
            elif(x%2 !=0):
                if(y%2==0):
                    if ch[i+x][j+y] == 'B':
                        c2+=1
                else:
                    if ch[i+x][j+y] == 'W':
                        c2+=1
    return min(c1,c2)
    

n, m = map(int,input().split())

ch = []
minN = 2500
for _ in range(n):
    ch.append(input())

for i in range(n-7):
    for j in range(m-7):
        ch[i][j]
        minN = min(minN, count(i,j))


print(minN)