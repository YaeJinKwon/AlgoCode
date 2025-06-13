n = input()

length = len(n)

left = list(map(int, n[0:length//2]))
right = list(map(int, n[length//2:]))

if (sum(left) == sum(right)):
    print("LUCKY")
else:
    print("READY")