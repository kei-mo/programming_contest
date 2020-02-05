N,M= map(int,input().split())
k_list = []
s_list = []
for _ in range(M):
    input_list = list(map(int,input().split()))
    k_list.append(input_list[0])
    s_list.append(input_list[1:])
p_list = list(map(int,input().split()))


on_num_dict = {} # それぞれの電球に対して、いくつのスイッチが押されていたらonになるかの辞書
for m in range(M):
    num_list = [i for i in range(k_list[m]+1) if i%2==p_list[m]]
    on_num_dict[m] = num_list

ans = 0
for i in range(2**N): # on off のパターン
    flag = 1
    bin_list = list(format(i, '0'+str(N)+'b')) # format(i, '02b') 
    for m in range(M): #電球ひとつひとつに対してon off を確認
        on_switch = [int(bin_list[s-1]) for s in s_list[m]] # switch の on off
        on_switch_num = sum(on_switch) # 
        if on_switch_num in on_num_dict[m]: # m番目の電球がonになるか否か
            flag = 1
        else: # offの場合はこのon offパターンの確認作業を終了する
            flag = 0
            break
    if flag == 1:
        ans+=1
print(ans)