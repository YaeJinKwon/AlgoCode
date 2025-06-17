import sys
input = sys.stdin.readline
score = {'A+' : 4.5, 'A0' : 4.0, 'B+':3.5, 
         'B0': 3.0, 'C+' : 2.5, 'C0' : 2.0,
          'D+' : 1.5, 'D0' : 1.0 , 'F' : 0.0 }


sumScore = 0
num = 0
while(True):
    s = input().split()
    if s == []:
        break
    if s[2] == 'P':
        continue
    num += float(s[1])

    sumScore += score[s[2]] * float(s[1])

print(sumScore/num)
    