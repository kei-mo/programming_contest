import math
def solve():
    N = int(input())
    
    low_b = 0
    high_b = 0
    pre_w = 0
    for i in range(N):
        a,b = map(int,input().split())
        w = a*c + b*j
        if w <= pre_w: # 今の比のままだと条件を満たさない
            if (a-pre_a) * (b-pre_b) <0: # aとbの比が逆
                cnt += 1
                if cnt >2:
                    return -1
            
            else:
            
                d = math.gcd(a,b)
                c = a//d
                j = b//d

            c = cand_c
            j = cand_j
            w = a*c + b*j
        pre_w = w    
        # pre_a, pre_b, pre_w = a,b,w

    return (c,j)
                


T = int(input())

for n in range(1,T+1):
    ans = solve()
    if ans == -1:
        print('Case #'+str(n)+': IMPOSSIBLE')
    else:
        print('Case #'+str(n)+': '+ str(ans[0])+' '+str(ans[1]))
