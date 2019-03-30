
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
        root_node0 = self.find_root(node0) 
        root_node1 = self.find_root(node1)

        if root_node0 != root_node1:
            # rankを比較しrankが小さい方の木を大きい方の木のrootにつなげる
            # rank is sameのときのみrankが増える
            if self.rank[root_node0] == self.rank[root_node1]: # rank is same
                self.parent[root_node1] = root_node0
                self.rank[root_node0] += 1
            elif self.rank[root_node0] > self.rank[root_node1]:
                self.parent[root_node1] = root_node0
            else:
                self.parent[root_node0] = root_node1

            self.size[root_node0] += self.size[root_node1]