import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())
print(math.comb(n , k))