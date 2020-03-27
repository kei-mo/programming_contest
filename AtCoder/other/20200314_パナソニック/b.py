H,W = map(int,input().split())
a = H*W
if (H==1 or W==1):
    print(1)
elif a%2 ==0:
    print(a//2)
else:
    print(a//2+1)