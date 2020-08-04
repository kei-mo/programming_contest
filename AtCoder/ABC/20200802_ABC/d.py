N = int(input())
string = input()
r2w = string.count("R")
w2r = 0
ans_list = [max(r2w, w2r)]
for c in string:
    if c == "W":
        w2r += 1
    else:
        r2w -= 1
    ans_list.append(max(r2w, w2r))
print(min(ans_list))