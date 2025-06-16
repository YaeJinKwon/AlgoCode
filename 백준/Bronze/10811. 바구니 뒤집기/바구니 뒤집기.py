import sys

input = sys.stdin.readline

n, m = map(int , input().split())

array = []
for i in range(n):
    array.append(i+1)

for _ in range(m):
    i, j = map(int , input().split())
    temp = array[i-1:j]
    temp.reverse()
    for k in range(len(temp)):
        array[i-1+k] = temp[k]

for i in array:
    print(i, end = " ")

