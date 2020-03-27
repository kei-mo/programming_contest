
a,b,c = map(int,input().split())

d=0
d+=a**2
d-=2*a*b
d+= b**2
d-= 2*b*c
d+= c**2
d-=2*c*a

if d>0.0:
    print('Yes')
else:
    print('No')