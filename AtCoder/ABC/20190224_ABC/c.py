N, A, B, C =map(int,input().split())
l = []
for i in range(N):
   a = int(input())
   l.append(a)

infty = 1000000

def DFS(i,uselist0,uselista,uselistb,uselistc):
   if i == N:
       return calc_mp(uselista,uselistb,uselistc)
   mplist = []
   u0 = uselist0 + [l[i]]
   ua = uselista + [l[i]]
   ub = uselistb + [l[i]]
   uc = uselistc + [l[i]]
   mplist.append(DFS(i+1, u0,uselista,uselistb,uselistc))
   mplist.append(DFS(i+1, uselist0,ua,uselistb,uselistc))
   mplist.append(DFS(i+1, uselist0,uselista,ub,uselistc))
   mplist.append(DFS(i+1, uselist0,uselista,uselistb,uc))
   return min(mplist)


def calc_mp(uselista,uselistb,uselistc):
   mp = 0
   #合成魔法
   mp += (max(len(uselista) - 1, 0)) * 10
   mp += (max(len(uselistb) - 1, 0)) * 10
   mp += (max(len(uselistc) - 1, 0)) * 10

   #その他魔法
   mp += abs(A - sum(uselista))
   mp += abs(B - sum(uselistb))
   mp += abs(C - sum(uselistc))

   if len(uselista)==0:
       mp += infty
   if len(uselistb)==0:
       mp += infty
   if len(uselistc)==0:
       mp += infty
   return mp

print(DFS(0,[],[],[],[]))
Message Input


Message #programing_contest