N,M = map(int,input().split())
s_list = []
c_list = []
for _ in range(M):
    s,c = input().split()
    s_list.append(int(s)-1)
    c_list.append(c)

ans = -1

if N ==1:
    num=str(0)
    flag = 1
    for j in range(M):
        s = s_list[j]
        c = c_list[j]
        if num[s]==c:
            pass
        else:
            flag=0
    if flag==1:
        ans = num
        
if ans ==-1:
    for i in range(10**(N-1),10**(N)):
        num = str(i)
        flag = 1
        for j in range(M):
            s = s_list[j]
            c = c_list[j]
            if num[s]==c:
                pass
            else:
                flag=0
        if flag==1:
            ans = num
            break
print(ans)
