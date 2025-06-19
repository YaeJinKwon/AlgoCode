n = int(input())


arr = []
for i in range(2666800):
    if(str(i).count('6') >= 3):
        t = 0
        for c in range (len(str(i))-2):
            if(str(i)[c] == '6' == str(i)[c+1] == str(i)[c+2]):
                arr.append(i)
                break

arr.sort()

print(arr[n-1])
