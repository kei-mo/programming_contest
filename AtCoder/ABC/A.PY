l = [int(input()) for _ in range(5)]
k = int(input())
max_dist = 0
max_dist = max(max_dist,l[4]-l[3])
max_dist = max(max_dist,l[4]-l[2])
max_dist = max(max_dist,l[4]-l[1])
max_dist = max(max_dist,l[4]-l[0])
max_dist = max(max_dist,l[3]-l[2])
max_dist = max(max_dist,l[3]-l[1])
max_dist = max(max_dist,l[3]-l[0])
max_dist = max(max_dist,l[2]-l[1])
max_dist = max(max_dist,l[2]-l[0])
max_dist = max(max_dist,l[1]-l[0])
if max_dist > k:
    ans = ':('
else:
    ans = 'Yay!'
print(ans)