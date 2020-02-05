a,b = map(int, input().split())
ans += max(a,b)
if ans ==a:
    ans+= max(a-1,b)
else:
    ans+= max(a,b-1)