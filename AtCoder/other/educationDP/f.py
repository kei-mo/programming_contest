### LCS 
# dp[i][j]: s[i],t[j]までの最長部分文字列の長さ
# s[i]==t[j]だったらs[i-1][j-1]+1,
# それ以外の場合はmax(s[i-1][j],s[i][j-1])

s= input()
t= input()

dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for i, si in enumerate(s):
    for j, tj in enumerate(t):
        if si==tj:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])

ans =""
n = dp[-1][-1]
i = len(s)
j =len(t)
while n >0:
    if dp[i][j]==dp[i-1][j]:
        i-= 1
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    elif dp[i][j]==dp[i-1][j-1]+1:
        ans = s[i-1]+ans
        n-=1
        i-=1
        j-=1

print(ans)

