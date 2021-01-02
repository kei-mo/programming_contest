N = int(input())
x_list = []
y_list = []
for _ in range(N):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

ans = 0
for i in range(N-1):
    xi = x_list[i]
    yi = y_list[i]
    for j in range(i+1,N):
        xj = x_list[j]
        yj = y_list[j]

        a = (yj-yi)/(xj-xi)
        if (a<=1 and a>=-1): 
            ans+=1
print(ans)