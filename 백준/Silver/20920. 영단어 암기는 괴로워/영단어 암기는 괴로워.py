import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = dict()
for _ in range(n):
    a = input().rstrip()
    if(len(a)< k):
        continue
    if a in arr:
        arr[a] +=1
    else:
        arr[a] = 1

data = []

for i in arr.keys():
    data.append((arr[i], i))

data.sort(key = lambda x : (-x[0], -len(x[1]), x[1]))


for i in data:
    print(i[1])
