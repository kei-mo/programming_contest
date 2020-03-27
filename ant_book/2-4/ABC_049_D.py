
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
        self.parent =[x for x in range(node_size)]
        self.node_size = node_size
        self.size = [1] * node_size
        self.rank = [1] * node_size

        # self.node_list = np.array([x for x in range(node_size)])
        self.member_dict = {}
    
    def find_root(self,node):
        # node属する木のrootを探す
        # たどった経路に含まれるnodeの親をrootにつなぎ替える
        if self.parent[node] == node:             # 自身がrootの場合
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




N,K,L = map(int,input().split())

road_uft = UnionFindTree(N)
train_uft = UnionFindTree(N)

for _ in range(K):
    p,q = map(int,input().split())
    p -=1
    q -=1
    road_uft.unite(p,q)

for _ in range(L):
    r,s = map(int,input().split())
    r-=1
    s-=1
    train_uft.unite(r,s)


pair_dict = {}
pair_list = []
for i in range(N):
    road_root = road_uft.find_root(i)
    train_root = train_uft.find_root(i)
    pair = (road_root,train_root)
    pair_list.append(pair)
    if pair in pair_dict:
        pair_dict[pair] +=1
    else:
        pair_dict[pair] = 1

ans = ""
for i in range(N):
    pair = pair_list[i]
    ans += str(pair_dict[pair]) + " "
print(ans)