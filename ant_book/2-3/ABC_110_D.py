import collections
N,M  = map(int,input().split())
mod = pow(10, 9) + 7

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def combination(n, r):
    ans = n
    for i in range(1, r):
        ans = ans * ((n - i) % mod) * pow(i + 1, mod - 2, mod)
        ans = ans % mod    
    return ans

c = collections.Counter(prime_factorize(M))

ans = 1
for num in c.values():
    ans = ans * combination(N - 1 + num, num)
    ans = ans % mod
print(ans)