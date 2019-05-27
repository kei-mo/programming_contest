from fractions import gcd
N = int(input())
A = list(map(int,input().split()))

l=[0]*N
r=[0]*N
l[0]=A[0]
r[0]=A[N-1]
for i in range(1,N-1):
   l[i]=gcd(l[i-1],A[i])
   r[i]=gcd(r[i-1],A[N-1-i])
gcdlist = [1,l[N-2],r[N-2]]
for i in range(N-2):
   gcdlist.append(gcd(l[i],r[N-3-i]))

print(max(gcdlist))