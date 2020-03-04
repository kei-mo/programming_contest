
class UnionFindTree():
    # Union find tree
    # 2つの効率化　経路圧縮、ランク
    # つなげることはできるか分離することはできないので、木をつなげる方向に利用する
    # 
    def __init__(self, node_size):
        # node_num: 全体のノード数
        # parent: ノードがrootなら-1、親がいれば親の番号を入れる
        # size:
        # rank:  
        # self.parent =[-1] * node_size
        self.parent =[-1]*node_size
 
        self.size = [1] * node_size
        self.rank = [1] * node_size
    
    def find_root(self,node):
        # node属する木のrootを探す
        # たどった経路に含まれるnodeの親をrootにつなぎ替える
        if self.parent[node] == -1:             # 自身がrootの場合
            root = node
        else:                                   # 自身がrootでない場合
            root = self.find_root(self.parent[node]) # 再帰的にrootを探す
            self.parent[node] = root            # たどった経路に含まれるnodeの親をrootにつなぎ替える(経路圧縮)
        return root

    def unite(self,node0, node1):
        # node0とnode1が含まれる木を結合する
        
        #node0 node1のrootを求める
        root_node0 = self.find_root(node0) 
        root_node1 = self.find_root(node1)

        if root_node0 != root_node1:
            # rankを比較しrankが小さい方の木を大きい方の木のrootにつなげる
            # rank is sameのときのみrankが増える

            # node1のグループをnode0のグループに結合
            if self.rank[root_node0] == self.rank[root_node1]: # rank is same
                self.parent[root_node1] = root_node0
                self.rank[root_node0] += 1
                self.size[root_node0] += self.size[root_node1]

            # node1のグループをnode0のグループに結合
            elif self.rank[root_node0] > self.rank[root_node1]:
                self.parent[root_node1] = root_node0
                self.size[root_node0] += self.size[root_node1]

            # node0のグループをnode1のグループに結合
            else:
                self.parent[root_node0] = root_node1
                self.size[root_node1] += self.size[root_node0]

    def same(self,node0,node1):
        #同じグループか確かめる
        return self.find_root(node0)==self.find_root(node1)


N,M,K = map(int,input().split())

ut = UnionFindTree(N)
friend_dict = {i:0 for i in range(N)}

for i in range(M):
    x,y = map(int,input().split())
    x-=1
    y-=1
    ut.unite(x,y)
    friend_dict[x]+=1
    friend_dict[y]+=1
    # friend_dict[x].extend([y])
    # friend_dict[y].extend([x])

# for i in range(N):
#     ut.find_root(i)

# block_dict = {i:[] for i in range(N)}
block_dict = {i:0 for i in range(N)}

for i in range(K):
    x,y = map(int,input().split())
    x-=1
    y-=1
    if ut.same(x,y):
        block_dict[x]+=1
        block_dict[y]+=1
        # block_dict[x].extend([y])
        # block_dict[y].extend([x])

ans =""
for i in range(N):
    group =  ut.find_root(i)
    group_size = ut.size[group]

    # cand = group_size - len(friend_dict[i]) - len(block_dict[i])
    cand = group_size - friend_dict[i] - block_dict[i] - 1
    ans += str(cand) + " "
print(ans)