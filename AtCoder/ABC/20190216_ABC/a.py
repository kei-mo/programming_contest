A, B = map(int,input().split())

c = B % A
if c ==0:
    ans = A+B
else:
    ans = B-A

print(ans)