

def solve():
        

T = int(input())

for n in range(1,T+1):
    ans = solve()
    if ans==np.inf:
        print('Case #'+str(n)+': IMPOSSIBLE')
    else:
        print('Case #'+str(n)+': '+ str(ans))
