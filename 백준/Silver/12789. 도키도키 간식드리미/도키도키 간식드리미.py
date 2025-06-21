import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))

count = 1
arr = []
for i in range(n):
    if(c[i] == count):
        count+=1
        while arr and arr[-1] == count:
            arr.pop()
            count += 1 
        continue
    else:
        arr.append(c[i])


if arr:
    print("Sad")
else:
    print("Nice")
        
