def dfs(cur,s1,s2):
    '''
    args
    cur: ノードの深さ
    s1, s2, ...: 取りうる枝分かれ
    '''
    if cur == N:
        return # 最後まで行ったら
    
    dfs() # 枝1
    dfs() # 枝2