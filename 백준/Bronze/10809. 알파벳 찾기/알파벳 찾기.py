s = input()

for i in range(0, 26):
    print(s.find(chr(ord('a')+i)), end = " ")