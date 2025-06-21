import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    data = input().rstrip()
    arr = []
    check = True
    if data[0] == ')':
        print('NO')
        continue
    for i in data:
        if i == ')':
            if arr:
                arr.pop()
            else:
                print('NO')
                check = False
                break
        else:
            arr.append(i)

    if len(arr)==0 and check:
        print("YES")
    elif check:
        print("NO")
