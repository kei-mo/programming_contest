import collections

N = int(input())
c_list = [int(input()) for _ in range(N)]

c = collections.Counter(c)

def DFS():

    most_common = c_list.most_common()[0]
    if most_common[1]>=2:
        
    return 

