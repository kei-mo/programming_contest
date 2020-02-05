trees = []
trees_ref = []
n,m = map(int, input().split())
ref = [1 for i in range(n)] ## 単一ノードを調べるために
 
s,e = map(int, input().split())
## 繋がれたものは消す
ref[s-1] = 0
ref[e-1] = 0
trees.append({s,e})
trees_ref.append(1)
    
for i in range(m-1):
    s,e = map(int, input().split())
    ## 繋がれたものは消す
    ref[s-1] = 0
    ref[e-1] = 0
    flag = 1
    ## 既にあるノードかを調べる
    for j in range(len(trees)):
        t = trees[j]
        if s in t:
            flag=0
            flag2=1
            for k in range(len(trees)):
                subt = trees[k]
                if (e in subt) and j==k: ## 同じ木の中で繋がれていたら
                    flag2 = 0
                    trees_ref[j] = 0
                elif e in subt:
                    flag2 = 0
                    trees[j] = trees[j].union(trees[k])
                    trees_ref[j] = int(trees_ref[j]+trees_ref[k]>1)
                    del trees[k]
                    del trees_ref[k]
            if flag2==1:
                trees[j].add(e)
                break
        if e in t:
            flag=0
            trees[j].add(s)
            break
    if flag==1:    ## 新規の木
        trees.append({s,e})
        trees_ref.append(1)
    
print(sum(ref)+sum(trees_ref))