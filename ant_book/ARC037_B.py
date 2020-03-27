N, M= map(int,input().split())

def search(x,group_list):
    for i, group in enumerate(group_list):
        if x in group:
            return i 
    return -1 # 見つからなかった場合

group_list = []
num_list = set()

for _ in range(M):
    u,v = map(int,input().split())
    num_list = num_list | set([u,v])

    u_group = search(u,group_list)
    v_group = search(v,group_list)

    if u_group ==-1 and v_group ==-1: # どちらにもない
        group_list.append(set([u,v]))

    elif u_group!=-1 and v_group==-1: # uだけある
        group_list[u_group].add(v)

    elif u_group ==-1 and v_group!=-1: # vだけある
        group_list[v_group].add(u)

    elif u_group !=-1 and u_group==v_group: # どちらも同じグループにある　すなわち閉路
        group_list[u_group].add(-1) # 閉路フラグ

    else:  # 別々のグループにある　つなげる
        group_list[v_group] = group_list[v_group] | group_list[u_group]
        del group_list[u_group]

ans = 0
for g in group_list:
    if -1 not in g:
        ans+=1

ans += N-len(num_list)
print(ans)
        