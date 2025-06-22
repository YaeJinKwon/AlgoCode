import sys
input = sys.stdin.readline

n, k = map(int,input().split())
A = list(map(int,input().split()))

c= 0
def mergeSort(A, p, r):
    if(p<r):
        q = (p+r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 1
    tmp = []
    global c

    while(i <= q and j <= r):
        if(A[i] <= A[j]):
            tmp.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            j+=1
    while (i<=q):
        tmp.append(A[i])
        i+=1
    while(j<=r):
        tmp.append(A[j])
        j+=1
    i = p
    t = 0
    while(i<=r):
        c+=1
        A[i] = tmp[t]
        if(c == k):
            print(A[i])
            break
        i+=1
        t+=1

mergeSort(A,0,n-1)
if(c < k):
    print(-1)