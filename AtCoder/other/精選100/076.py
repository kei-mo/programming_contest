N = int(input())
a_list = list(map(int,input().split()))

for k in range(N):
    x = sum(a_list[:k+1])
    max_x = x
    for i in range(k+1,N):
        y = a_list[i]
        z = a_list[i-k-1]
        x += y-z
        if x>max_x:
            max_x = x
    print(max_x)
