N,A,B,C = map(int,input().split())



def s3(abc_dict):
    ans = []
    for _ in range(N):
        xy = input()
        x = xy[0] 
        y = xy[1]
        if abc_dict[x]==0 and abc_dict[y]==0:
            return False, []
        elif abc_dict[x]>=abc_dict[y]:
            abc_dict[x] -= 1
            abc_dict[y] += 1
            ans.append(y)
        else:
            abc_dict[y] -= 1
            abc_dict[x] += 1
            ans.append(x)
    return True, ans

def s2(abc_dict):

    ans = []
    flag = True
    q_list = []
    for _ in range(N):
        q_list.append(input())

    for i in range(N):
        xy = q_list[i]
        x = xy[0]
        y = xy[1]

        if (abc_dict[x]>=1 and abc_dict[y]==0):
            abc_dict[x]-=1
            abc_dict[y]+=1
            ans.append(y)
        elif (abc_dict[y]>=1 and abc_dict[x]==0):
            abc_dict[y]-=1
            abc_dict[x]+=1
            ans.append(x)
        elif  (abc_dict[x]==1 and abc_dict[y]==1):
            if i==N-1:
                ans.append(x)
            else:
                next_xy = q_list[i+1]
                if xy==next_xy: # 次も同じなのでどちらでもいい
                    abc_dict[x]+=1
                    abc_dict[y]-=1
                    ans.append(x)
                elif (x in next_xy):
                    abc_dict[x]+=1
                    abc_dict[y]-=1
                    ans.append(x)
                else: # 次にyが含まれる
                    abc_dict[y]+=1
                    abc_dict[x]-=1
                    ans.append(y)
        else:
            return False, []
    return True,ans

def s1(abc_dict):
    
    ans = []
    flag = True
    for _ in range(N):
        xy = input()
        x = xy[0] 
        y = xy[1]
        if abc_dict[x]==1:
            abc_dict[x]-=1
            abc_dict[y]+=1
            ans.append(y)
        elif abc_dict[y]==1:
            abc_dict[y]-=1
            abc_dict[x]+=1
            ans.append(x)
        else:
            flag = False
            return flag,[]
    return flag, ans
    
def s0(abc_dict):
    return False, []

abc_dict = {"A":A,"B":B,"C":C}
sumABC = A+B+C
if sumABC>=3:
    flag, ans = s3(abc_dict)
elif sumABC==2:
    flag, ans = s2(abc_dict)
elif sumABC==1:
    flag, ans = s1(abc_dict)
elif sumABC==0:
    flag, ans = False, []

if flag:
    print('Yes')
    for i in range(N):
        print(ans[i])
else:
    print("No")  