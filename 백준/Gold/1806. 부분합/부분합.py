import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))

ans = []
end = 0
sum = 0
for start in range(N):
    while(sum < S and end <N):
        sum += arr[end]
        end +=1
    if(sum>=S):
        ans.append(end-start)
    sum -= arr[start]

ans.sort()
if ans:
    print(ans[0])
else:
    print(0)

