i = 0
a = []
for _ in range(3):
    a.append(int(input()))
a.sort()

if(a.count(60) == 3):
    print("Equilateral")
elif(sum(a) == 180 and (a[0]==a[1] or a[1] == a[2])):
    print("Isosceles")
elif(sum(a) == 180):
    print("Scalene")
else:
    print("Error")