S,T = input().split()
s_num,t_num = map(int,input().split())
U = input()

if S==U:
    print(str(s_num-1)+" "+str(t_num))
else:
    print(str(s_num)+" "+str(t_num-1))
    