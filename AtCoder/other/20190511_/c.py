N = int(input())
s_list = [input() for _ in range(N)]
end_a_num = 0
start_b_num = 0
same_num = 0
ans = 0
for s in s_list:
    ab_num = s.count('AB')
    ans += ab_num
    if s[-1] == 'A':
        end_a_num+=1
    if s[0]=='B':
        start_b_num+=1
    if s[-1]=='A' and s[0]=='B':
        same_num+=1


ans+= min(end_a_num,start_b_num)
if end_a_num==start_b_num and end_a_num==same_num and same_num>0:
    ans-=1

print(ans)