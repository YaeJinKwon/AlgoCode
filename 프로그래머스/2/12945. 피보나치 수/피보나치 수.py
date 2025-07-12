def solution(n):
    t = 2
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    while(t <= n):
        f[t] = f[t-2]+ f[t-1]
        t+=1

    answer = f[n]%1234567
    return answer