import sys
input = sys.stdin.readline

n = int(input())

data = []

for _ in range(n):
    data.append(int(input()))

print(round(sum(data) / n))
data.sort()
print(data[n//2])

find = dict()

for i in data:
    if i in find:
        find[i] += 1
    else:
       find[i] = 1 

arr = []
for i in find.keys():
    arr.append((find[i], i))

arr.sort(key=lambda x : x[0], reverse = True)
if (len(arr) > 1 and arr[0][0] == arr[1][0]):
    print(arr[1][1])
else: print(arr[0][1])

print(max(data) - min(data))

