from math import factorial

n,a,b = map(int,input().split())

mod = 10**9+7

def comb(n,k,p):
  """power_funcを用いて(nCk) mod p を求める"""
  x = 1
  y = 1
  for i in range(k):
    x= (x *(n-i))%p
    y= (y* (k-i))%p
  yinv = pow(y,p-2,p)
  return (x*yinv)%p


ans = (pow(2,n,mod)- 1 - comb(n,a,mod)-comb(n,b,mod))%mod
print(ans)