N = int(input())
alphabets = ['a','b','c','d','e','f','g','h','i','j']

ans_list = [['a',0]]

for i in range(1,N):
    pre_ans_list = ans_list.copy()
    ans_list = []
    for word_info in pre_ans_list:
        word = word_info[0]
        max_word = word_info[1] # 今まで出てきたなかで一番大きいもの
        postfix = alphabets[:min(i,max_word+1)+1]
        for j,p in enumerate(postfix):
            ans_list.append([word+p,max(j,max_word)])
for a in ans_list:
    print(a[0])
                

