#n,k=map(int,input().split())
#a=list(map(int,input().split()))

n,k = 4,9
a = [7, 4, 0, 3]

t,ans=2**40,0
while t:
	c=sum([(a[i]&t)//t for i in range(n)])
	if k<t or c*2>=n:
		ans+=t*c
	else2:
		ans+=t*(n-c)
		k -= t
	t //= 2
print(ans)