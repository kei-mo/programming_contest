# Pylons
T = int(input())

def canvisit(pos,prepos):
    if pos[0]==prepos[0]:
        return False
    if pos[1]==prepos[1]:
        return False
    if pos[0]-pos[1]==prepos[0]-prepos[1]:
        return False
    if pos[0]+pos[1]==prepos[0]+prepos[1]:
        return False
    return True

# def getNextColumn(notvisited,end_pos):
#     return next_c

def solve(r,c):

    # 長い方を列として扱う
    transpose = False
    if r>c:
        transpose = True
    long_side = max(r,c)
    short_side = min(r,c)


    if (r<=3 and c<=3):
        return False,[],transpose
    
    ans_list = []



    #方針:前の行で訪れた列+2を次の行で訪れる
    # end_pos = [short_side,-1*long_side]
    
    if long_side%2==0:
        start_c = 1
    else:
        start_c = 1 # int((long_side+1)/2)

    notvisited = [x for x in range(1,long_side+1) if x!=start_c] 
    for i in range(long_side):

        if i!=0:
            start_c = 0
            for k,x in enumerate(notvisited):
                if canvisit([1,x],end_pos):
                    start_c = notvisited.pop(k)
                    ans_list.append([1,x])
                    break
            if start_c == 0: # 次の訪れることができる列がない
                return False,[],transpose
        
        pre_c = start_c 
        for j in range(2,short_side+1):
            if pre_c+2<=long_side: # 2個隣の列
                pre_c+=2                 
            else: # 回って1列もしくは2列め
                pre_c = pre_c+2-long_side


            ans_list.append([j,pre_c])
        end_pos = [short_side,pre_c]
    
    return True,ans_list,transpose
            
for n in range(1,T+1):
    r,c = map(int,input().split())
    ans,ans_list,transpose = solve(r,c)
    if ans:
        print('Case #'+str(n)+': POSSIBLE')
        if transpose:
            [print(x[1],x[0]) for x in ans_list]
        else:
            [print(x[0],x[1]) for x in ans_list]
    else:
        print('Case #'+str(n)+': IMPOSSIBLE')


    

    

