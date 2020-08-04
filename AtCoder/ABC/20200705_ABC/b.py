N = int(input())

cnt_dict = {"AC":0,"WA":0,"TLE":0,"RE":0}
for i in range(N):
    s = input()
    cnt_dict[s] += 1

for s in ["AC", "WA", "TLE", "RE"]:
    print(f"{s} x {cnt_dict[s]}")
