A,B,K = map(int,input().split())

a = max(0,A-K)
b = max(0,B-max(K-A,0))
print(str(a) + " "+str(b))
