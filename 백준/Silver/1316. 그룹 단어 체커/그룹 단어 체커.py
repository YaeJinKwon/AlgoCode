n = int(input())

answer  = n
for _ in range(n):
    s = input()
    for i in s:
        first = s.index(i)
        last = s.rindex(i)
        c = s.count(i)
        if (last - first +1) != c :
            answer -= 1
            break
    
    
print(answer)