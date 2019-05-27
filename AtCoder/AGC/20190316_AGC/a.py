N = int(input())
S = input()

used_list = []
num = 0
a = 10**9 +7 

def DFS(i,used_list,num):
    if i == N:
        num += 1
        num = num % a
        return num

    s = S[i]
    # S[i]を使わない場合
    num = DFS(i+1,used_list,num) % a

    # S[i]を使う場合
    if s not in used_list:
        used_list.append(s)
        num=DFS(i+1,used_list,num) % a

        used_list.pop(-1)
    return num
    
       
ans = DFS(0,used_list,num)
ans = ans-1

print(ans)