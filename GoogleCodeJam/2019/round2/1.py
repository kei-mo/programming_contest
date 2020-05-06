import math
def solve():
    N = int(input())
    n_list = []
    for i in range(N):
        n_list.append(list(map(int,input().split())))

    ratio_set = set() # 大小関係が切り替わるポイントを格納する
    for i in range(N-1):
        x = n_list[i]
        for j in range(i+1,N):
            y = n_list[j]
            a = x[0]-y[0]
            b = y[1]-x[1]
            if a*b>0:
                c = math.gcd(abs(a),abs(b))
                ratio_set.add((a//c,b//c))
            # a = (x[0]-y[0]) * 1000000000000000
            # b = y[1]-x[1]
            # ratio = 0.0
            # if b!=0:
            #     a = float(a)
            #     b = float(b)
            #     ratio = a/b
            # if ratio>0.0:
            #     ratio_set.add(ratio)
    return 1+len(ratio_set)
                


T = int(input())

for n in range(1,T+1):
    ans = solve()
    print('Case #'+str(n)+': '+ str(ans))
