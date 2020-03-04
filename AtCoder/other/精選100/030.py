N=int(input())
num_list = list(map(int,input().split()))
count_dict = {}
for i in range(21):
    count_dict[str(i)]=0

dp = [count_dict.copy() for _ in range(N-1)]

for i in range(N-1):
    if i ==0:
        dp[i][str(num_list[i])] +=1
    else:
        for n in range(21):
            pre_count = dp[i-1][str(n)]

            post0 = n+num_list[i]
            post1 = n-num_list[i]
            if post0<=20:
                dp[i][str(post0)] +=pre_count
            if post1>=0:
                dp[i][str(post1)] +=pre_count
ans = dp[-1][str(num_list[-1])]
print(ans)