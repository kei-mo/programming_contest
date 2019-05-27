import bisect

A, B, Q = map(int,input().split())
INF = 10**18
s = [-INF] +  [int(input()) for i in range(A)] + [INF]
t = [-INF] + [int(input()) for i in range(B)] + [INF]
x_list = [int(input()) for i in range(Q)]

for x in x_list:
    
    b, d = bisect.bisect_right(s, x), bisect.bisect_right(t, x)
    a = b - 1
    c = d - 1 
    ans = min(abs(s[a]-x) + min(abs(t[c]-s[a]), abs(t[d]-s[a])),
              abs(s[b]-x) + min(abs(t[c]-s[b]), abs(t[d]-s[b])),
              abs(t[c]-x) + min(abs(s[a]-t[c]), abs(s[b]-t[c])),
              abs(t[d]-x) + min(abs(s[a]-t[d]), abs(s[b]-t[d])))

    # for s in [s_list[a], s_list[b]]:
    #     for t in [t_list[c], t_list[d]]:
    #         dist1 = abs(s-x) + abs(t-s)
    #         dist2 = abs(t-x) + abs(t-s)
    #         ans = min(ans, dist1,dist2)
    print(ans)
