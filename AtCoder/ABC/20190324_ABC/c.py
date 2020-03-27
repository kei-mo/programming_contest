N, Q = map(int,input().split())
S= input()
lr_list = [list(map(int,input().split())) for _ in range(Q)]
for i in range(Q):
    l = lr_list[i][0] -1
    r = lr_list[i][1] -1
    s = S[l:r+1]
    ans = s.count('AC')
    print(ans)
