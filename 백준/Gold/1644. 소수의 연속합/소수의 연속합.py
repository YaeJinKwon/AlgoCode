import sys
input = sys.stdin.readline

N = int(input())
arr = []
is_prime = [True] * (N+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int((N+1)**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False
for i in range(2, N+1):
    if is_prime[i]:
        arr.append(i)


count = 0
end = 0
sum = 0
for start in range(len(arr)):
    while(sum < N and end <len(arr)):
        sum += arr[end]
        end +=1
    if(sum==N):
        count +=1
    sum -= arr[start]


print(count)


