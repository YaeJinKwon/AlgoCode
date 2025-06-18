
while(True):
    a, b, c = map(int,input().split())
    if a == b == c == 0:
        break
    m = max(a,b,c)
    if(m >= a + b +c - m ):
        print("Invalid")
        continue
    if a == b == c:
        print("Equilateral")
    elif a == b != c or a != b == c or a == c != b :
        print("Isosceles")
    elif a!= b != c:
        print("Scalene")
    