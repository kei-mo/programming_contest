S  = input()
n = len(S)-1

def sum_s(s):
    return sum(list(map(int,s.split("+"))))

def dfs(i,s,m): 
    #
    #
    # m: これまでに何回
    ans = 0
    if i==n:
        return sum_s(s)

    ans += dfs(i+1,s,m) # i番目に+を入れない場合
    ans += dfs(i+1,s[:i+1+m]+"+"+s[i+1+m:],m+1) # i番目に+を入れる場合

    return ans


print(dfs(0,S,0))