from itertools import combinations
n, m= map(int, input().split())

card = list(map(int,input().split()))

total = list(combinations(card,3))
total = list(map(sum, total))

total.sort()

answer = 0
for i in range(len(total)):
    if(total[i]>m):
        answer = total[i-1]
        break
if answer == 0:
    print(total[-1])
else:
    print(answer)