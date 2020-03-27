N= int(input())
if N%2==0:
    cand = list(range(1,N,2))
else:
    cand = list(range(1,N+1,2))

ans = 0
num = 0
for n in range(1,N+1):
    num = 0
    for c in cand:
        if n%c==0:
            num+=1
    if num ==8:
        ans+=1
print(ans)

    