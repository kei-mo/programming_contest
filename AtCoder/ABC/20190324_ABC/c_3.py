N, Q = map(int,input().split())
S= input()
lr_list = [list(map(int,input().split())) for _ in range(Q)]

# ac_tf_list = [1 if S[i:i+2]=='AC' else 0 for i in range(N-1)]
t = [0]*N
for i in range(N-1):
    if S[i:i+2]=='AC':
        t[i+1] = t[i]+1
    else:
        t[i+1] = t[i]

for i in range(Q):
    l = lr_list[i][0]-1
    r = lr_list[i][1]-1
    print(t[r]-t[l])
