NM = list(map(int,input().split()))
N,M = NM[0], NM[1]
li = list(map(int,input().split()))

if N>=M:
    ans = 0
else:
    li.sort()
    diff = []
    for i in range(M-1):
        diff.append(li[i+1]-li[i])
    diff.sort()
    ans = sum(diff[:-(N-1)])
print(ans)