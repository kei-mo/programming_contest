
N = int(input())
n_list = list(input())


def d(N,n_list):
    # 答えの偶数奇数の判断
    half = N//2
    


def f(N,n_list):
    sym=True
    half = N//2

    for i in range(half):
        pre = str(abs(int(n_list[i])-2))
        post = str(abs(int(n_list[-(i+1)])-2))
        if pre!=post:
            sym = False
    if sym:
        ans=0
    else:
        if "2" in n_list:
            ans=1
        else:
            ans=2
    return ans 

if N%2==1:
    ans = f(N,n_list)
else:
    ans = abs(f(N-1,n_list[1:]) - f(N-1,n_list[:-1]))

print(ans)