import math
def solution(m, n, startX, startY, balls):
    
    answer = []
    for ball in balls:
        minA = 1e9
        if(startY == ball[1]):
            minA = min(minA, (startX-ball[0])**2 + (2*(n-startY))**2)
            minA = min(minA, (startX-ball[0])**2 + (2*startY)**2)
            if(startX > ball[0]):
                minA = min(minA, ((2*m-startX)-ball[0])**2)
            else:
                minA = min(minA, (startX + ball[0])**2)
        elif(startX == ball[0]):
            minA = min(minA, (startY-ball[1])**2 + (2*(m-startX))**2)
            minA = min(minA, (startY-ball[1])**2 + (2*startX)**2)
            if(startY > ball[1]):
                minA = min(minA, ((2*n-startY)-ball[1])**2)
            else:
                minA = min(minA, (startY + ball[1])**2)
        else:
            minA = min(minA, (startX-ball[0])**2 + (startY-(2*n-ball[1]))**2)
            minA = min(minA, (startX-(2*m - ball[0]))**2 + (startY-ball[1])**2)
            minA = min(minA, (startX+ball[0])**2 + (startY-ball[1])**2)
            minA = min(minA, (startX-ball[0])**2 + (startY+ball[1])**2)

        answer.append(minA)
        
    return answer