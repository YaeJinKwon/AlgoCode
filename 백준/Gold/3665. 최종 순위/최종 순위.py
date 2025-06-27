import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())

    graph = [[] for _ in range (n+1)]
    data = [0]*(n+1)

    for i in range(n-1):
        for j in range(i+1, n):
            graph[arr[i]].append(arr[j])
            data[arr[j]] +=1
    
    for i in range(m):
        a, b = map(int,input().split())
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            data[b] +=1
            data[a] -= 1
        else: 
            graph[a].remove(b)
            graph[b].append(a)
            data[a] +=1
            data[b] -= 1
 
    imp = False
    know = False

    find = deque()
    for i in range(1, len(data)):
        if data[i] == 0:
            find.append(i)

    if not find:
        imp = True
    
    ans = []
    while(find):
        if len(find)>1:
            know = True
        s = find.popleft()
        ans.append(s)
        for i in graph[s]:
            data[i] -= 1
            if data[i] == 0:
                find.append(i)
    if len(ans) != n or imp:
        print("IMPOSSIBLE")
    elif know:
        print("?")
    else:
        print(*ans)


        