import collections

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

N = int(input())
c = collections.Counter(prime_factorize(N))

def getCount(w):
    i = 1
    n = 1
    while n <= w:
        i+=1
        n+=i
    return i - 1

cnt = 0

for v in c.values():
    cnt += getCount(v)

print(cnt)