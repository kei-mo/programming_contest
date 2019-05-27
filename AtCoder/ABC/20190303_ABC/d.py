
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
        self.parent =[-1] * node_size 
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
        root0 = self.find_root(node0) 
        root1 = self.find_root(node1)

        if root0 != root1:
            # rankを比較しrankが小さい方の木を大きい方の木のrootにつなげる
            # rank is sameのときのみrankが増える
            rank0 = self.rank[root0]
            rank1 = self.rank[root1]

            if rank0 == rank1: # rank is same
                self.parent[root1] = root0
                self.size[root0] += self.size[root1]
                self.rank[root0] += 1
            elif rank0 > rank1:
                self.parent[root1] = root0
                self.size[root0] += self.size[root1]
            else:
                self.parent[root0] = root1
                self.size[root1] += self.size[root0]

            


N,M = map(int,input().split())
bridges = [list(map(int,input().split())) for i in range(M)]

UFT = UnionFindTree(N)

a = int(N*(N-1)/2) # 不便さ
ans = [a]

for i in range(1,M)[::-1]:
    island0_num, island1_num = bridges[i][0]-1, bridges[i][1]-1 
    root0 = UFT.find_root(island0_num)
    root1 = UFT.find_root(island1_num)
    if root0 != root1:
        size0 =  UFT.size[root0]
        size1 =  UFT.size[root1]
        UFT.unite(island0_num,island1_num)
        a -= size0 * size1
    ans.append(int(a))

[print(ans[i]) for i in range(M)[::-1]]
