N = int(input())
tree = {i:{} for i in range(1,1+N)}
for i in range(N-1):
    a,b,c = map(int, input().split())
    tree[a][b] = c
    tree[b][a] = c
#print(tree)
Q, K = map(int, input().split())
 
#Kから各点までの距離を求めていく
k_dst = {}
 
def p_dist(node, dist):
    if len(tree[node]) == 0:
        k_dst[node] = dist
        #print("k_dst %d : %d"%(node,dist))
    while len(tree[node]) != 0:
        i = list(tree[node].keys())[0]
        c = tree[node][i]
        del tree[node][i]
        del tree[i][node]
        k_dst[i] = dist + c
        p_dist(i, dist + c)
        #print("k_dst %d : %d"%(i,k_dst[i]))
 
p_dist(K,0)
 
for i in range(Q):
    x,y = map(int, input().split())
    print(k_dst[x]+k_dst[y])