N,M= map(int,input().split())
x_list = []

for _ in range(M):
    x_list.append(list(map(int,input().split())))

ans = 1
for bit in range(pow(2,N)):
    num = bin(bit).count("1")
    if (num>ans and num>=2):
        flag = 1
        friends = []
        for i in range(N):
            if (bit & 1<<i)==1<<i:
                friends.append(i+1)
    
        for i in range(num-1):
            for j in range(i+1,num):
                if [friends[i],friends[j]] not in x_list:
                    flag=0

        if flag==1:
            ans = num
print(ans)

