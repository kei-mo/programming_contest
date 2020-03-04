N, M= map(int,input().split())
path_dict = {}
for n in range(1,N+1):
    path_dict[n] = []
for _ in range(M):
    u,v = map(int,input().split())
    path_dict[u].append(v)
    path_dict[v].append(u)

unexplored = set(list(range(1,N+1)))
# edges = [tuple(map(int,input().split())) for _ in range(M)]

def dfs(i,pre_node,explored,ng_nodes):
    
    # i: 現在のノード
    # pre_node: 直前のノード
    # explored: これまでに探索したノード
    # ng_nodes: 閉路木に含まれるノード
    # flag: 0閉路 
    explored.append(i)
    next_nodes_cand = path_dict[i].copy() # 次の行き先候補
    if pre_node is not None: # startではない場合、直前に訪れたノードを外す
        next_nodes_cand.remove(pre_node) 

    
    ### 深堀り終了要件 ###
    if len(set(next_nodes_cand)&set(explored))>0: # 閉路検出
        flag = 0
        ng_nodes = ng_nodes | set(explored) # 閉路木に含まれるものを更新
        ng_nodes = ng_nodes | set(next_nodes_cand) # 閉路木に含まれるものを更新
        return flag, explored, ng_nodes
    if len(next_nodes_cand)==0: # 終点
        flag = 1 
        return flag, explored, ng_nodes
    ###  ###
    
    for nnode in next_nodes_cand:
        flag,explored,ng_nodes= dfs(nnode,i,explored,ng_nodes)
        if flag==0:
            return flag,explored,ng_nodes
        
    return flag,explored,ng_nodes

ans = 0
ng_nodes = set()
while len(unexplored)>0:
    start = unexplored.pop()
    explored = []
    flag,explored,ng_nodes = dfs(start,None,explored,ng_nodes)
    unexplored = unexplored - set(explored)
    if flag ==1:
        ans+=1

print(ans)


    
