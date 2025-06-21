import sys
input = sys.stdin.readline

while (True):
    data = input().rstrip()
    if data == '.': break
    arr = []
    for i in data:
        if i == ')':
            if arr and arr[-1] == '(':
                arr.pop()
            else :
                print('no')
                break
        elif i == ']':
            if arr and arr[-1] == '[':
                arr.pop()
            else :
                print('no')
                break

        elif i == '(':
            arr.append(i)
        elif i == '[':
            arr.append(i)
    else:
        if arr:
            print('no')
        else:
            print('yes')
