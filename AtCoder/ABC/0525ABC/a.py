A, B = map(int,input().split())
if A>12:
    ans = B
elif A>5:
    ans = B/2
else:
    ans = 0
print(int(ans))