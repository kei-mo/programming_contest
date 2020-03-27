li = list(map(int,input().split()))
li.extend(list(map(int,input().split())))
li.extend(list(map(int,input().split())))

num = []
for i in range(1,5):
    num.append(list.count(i))

if num.count(1) == 2 and num.count(2) == 2:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)