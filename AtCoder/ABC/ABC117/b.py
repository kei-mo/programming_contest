N  = int(input())
li = list(map(int,input().split()))
maxL = max(li)
if maxL < sum(li) - maxL:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)