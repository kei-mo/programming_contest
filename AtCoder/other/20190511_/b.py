R,G,B,N = map(int,input().split())
r_max = N//R

ans =0
for i in range(r_max+1):
    n_r = N-(R*i)
    if n_r==0:
        ans+=1
    else:
        g_max = n_r//G
        for j in range(g_max+1):
            n_g = n_r-G*j
            if n_g==0:
                ans+=1
            else:
                if n_g%B==0:
                    ans+=1
print(ans)
