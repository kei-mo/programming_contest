import math
A,B= map(int,input().split())
# min_x = math.ceil(max(A/8,B/10)*100) # これはNG
min_x = math.ceil(max(A/0.08,B/0.10)) # これはOK

max_x = (min((A+1)/8,(B+1)/10)*100)

if max_x-min_x>0:
    ans = int(min_x)
else:
    ans = -1
print(ans)