
a,b = input().split()

a = int(a)
b = int(b[0]+b[2]+b[3])

ans = str(a * b)
if len(ans)>=3:
    ans = ans[:-2]
else:
    ans = 0
print(ans)
