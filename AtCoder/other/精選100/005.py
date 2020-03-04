N = int(input())
S= input()
s_list= list(S)

ans = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            x= S[:-2].find(str(i))
            if x!=-1:
                y=S[x+1:-1].find(str(j))
                if y!=-1:
                    z=S[x+1+y+1:].find(str(k))
                    if z!=-1:
                        ans+=1

print(ans)