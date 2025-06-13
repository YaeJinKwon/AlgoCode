s = input()

d = s[0]
count = 1
for i in range(1, len(s)):
    if(d != s[i]):
        d = s[i]
        count += 1

print (count//2)