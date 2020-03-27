def main():
    N,S= map(int,input().split())
    a_list = list(map(int,input().split()))

    # dp[i][j]: i番目までの数字を使ってjを作るときの左右の数字ペア

    dp = [[[] for _ in range(S+1)] for _ in range(N)]


    ans=0
    pair_list = {}

    a0 = a_list[0]
    if a0<=S:
        dp[0][a0].append(0)
    if a0==S:
        pair_list[0] = [0]


    for i in range(1,N):
        a = a_list[i]
        for j in range(1,S+1):
            if j==S:
                l_list = []

                # i番目だけを使う場合
                if j==a:
                    l_list.append(i)
                pre_j = j-a
                # i-1番目以前と i番目を使う場合
                if pre_j>0:
                    l_list.extend(dp[i-1][pre_j])
                for l in l_list:
                    l+=1
                    r =i+1
                    ans+= l * (N-r+1)

            else:

                # i番目を使わない場合
                dp[i][j].extend(dp[i-1][j])

                # i番目だけを使う場合
                if j==a:
                    dp[i][j].append(i)

                # i-1番目以前と i番目を使う場合
                pre_j = j-a
                if pre_j>0:
                    dp[i][j].extend(dp[i-1][pre_j])
                
                    


                # pattern_list = dp[i-1][pre_j]
                # for p in pattern_list:
                #     left = p[0]
                #     dp[i][j].append([left,i])
    # pair_list = dp[-1][-1]
    # ans = 0

    # for i in pair_list.keys():
    #     r = i+1
    #     for j in pair_list[i]:
    #         l = j+1
    #         ans += l * (N-r+1)
    print(ans)


if __name__ == "__main__":
    main()        


