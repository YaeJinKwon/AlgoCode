import sys
import math
input = sys.stdin.readline


a, b = map(int,input().split())
c, d = map(int,input().split())

son = a*d+c*b
mother = b*d

x = math.gcd(son, mother)

son = son // x
mother = mother//x

print(son, mother)