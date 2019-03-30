#%%
#nk = list(map(int,input().split()))
nk = [4,9]

#%%
N,K = nk[0], nk[1]
Kbin = bin(K)[2:] # srt
len_Kbin = len(Kbin)


#%%
#Xs = list(map(int,input().split()))
Xs = [7, 4, 0, 3]
Xs_bin = [int(bin(X)[2:]) for X in Xs if X <=K]# int
Xs_bin_sum = sum(Xs_bin)
# Xs_bin_sum

#%%
ans1 = ''
for i in range(len_Kbin-1):
    if int(str(Xs_bin_sum)[-(i+1)]) < N/2:
        ans1 = '1' + flip
    else:
        ans1 = '0' + flip

best = '1' + ans1

ans2 = ''
for i in range(len_Kbin):
    if best[i] == Kbin[i]:
        ans2 = '1' + ans2
    else:
        ans2 = '0' + ans2

ans = max(int(ans1,2),int(ans2,2))
print(ans)




#%%
print(int(ans1,2))


#%%
