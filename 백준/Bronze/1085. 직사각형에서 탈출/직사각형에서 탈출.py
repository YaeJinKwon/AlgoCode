x, y , w, h = map(int , input().split())

ans = min(w - x, h -y, x, y)

print(ans)