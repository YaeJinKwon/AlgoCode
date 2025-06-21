import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    data = input().rstrip()
    arr = []
    if data[0] == ')':
        print('NO')
        continue
    for i in data:
        if i == ')':
            if arr:
                arr.pop()
            else:
                print('NO')
                break
        else:
            arr.append(i)

    else : 
        if len(arr)==0:
            print("YES")
        else : 
            print("NO")