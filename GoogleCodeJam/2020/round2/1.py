
import math

def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    if b**2-4*a*c>=0:
        D = math.sqrt(b**2 - 4*a*c)
        x_1 = (-b + D) / (2 * a)

        return x_1
    else:
        return 0

def solve():
    ans = 0
    l,r = map(int,input().split())
    if l>=r:
        trans = False
    else:
        trans = True
        l,r = r, l
    diff = l-r
    x1 = solv_quadratic_equation(1,1,-2*diff)

    x1 = math.floor(x1)
    if x1>0:
        l-= int(x1 *(x1+1) *0.5)
    ans += x1

    if (l==r and trans):
        l,r = r,l
        trans =False
    x2 = solv_quadratic_equation(1,x1,-l) # 交互に配り始めてから左側で配るヒトのにずう
    x2 = math.floor(x2)

    if x2>0:
        l -= x2*(x2+x1)
        ans += x2
    
    x3 =solv_quadratic_equation(1,x1+1,-r)  # 交互に配り始めたから右側wで配る人数
    x3 = math.floor(x3)
    if x3>0:
        
        r -= x3*(x3+x1+1)
        ans += x3
    
    if trans:
        return ans,r,l
    else:
        return ans,l,r



T = int(input())

for n in range(1,T+1):
    ans,l,r = solve()

    print('Case #{}: {} {} {}'.format(n,ans,l,r))
