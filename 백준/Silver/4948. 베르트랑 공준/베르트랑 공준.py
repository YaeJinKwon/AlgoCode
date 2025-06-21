import sys
input = sys.stdin.readline

MAX = 123456 * 2 + 1
is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체로 소수 미리 구하기
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    # n+1부터 2n까지 소수 개수 세기
    print(sum(is_prime[n+1:2*n+1]))

# 13 17 19 23