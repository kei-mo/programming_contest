import numpy as np


class BDF():
    def __init__(self):
        self.H, self.W = map(int,input().split())
        matrix = []
        for _ in range(self.H):

            matrix.append(list(input()))
        
        self.matrix = np.array(matrix)
        

        self.que = []
        self.count = []
        self.went = []
        
        self.white_list = []

        self.max_step = 0        
        self.terminal = False
        self.get_parent()

    def get_parent(self):
        white_list = np.where(self.matrix=='.')
        if len(white_list[0]) ==0:
            print(self.max_step)
            self.terminal = True
        else:
            parent = [white_list[0][0],white_list[1][0]]    
            self.matrix[parent[0],parent[1]] = "d"
            self.que.append(parent)
            self.count.append(0)

    
    def check(self,row,col):
        state = self.matrix[row,col]
        return state

    def end(self,count):
        total_count = count +1
        self.max_step = max(self.max_step,total_count)
        self.que.clear()
        self.count.clear()
        for pos in self.went:
            self.matrix[pos[0],pos[1]] = total_count
            total_count -= 1
        self.went.clear()
        self.get_parent()

    def bdf(self):
        # matrix = self.matrix
        cur_info = self.que.pop(0)
        count = self.count.pop(0)
        cur_row = cur_info[0]
        cur_column = cur_info[1]
        
        self.matrix[cur_row,cur_column] = "d"
        self.went.append([cur_row,cur_column])

        num = -1

        # 上を見る       
        if not cur_row == 0:
            state = self.check(cur_row-1,cur_column)
            if state == "#":
                self.end(count)
            elif state == ".":
                self.que.append([cur_row-1,cur_column])
                self.count.append(count+1)
            elif state == "d":
                pass
            else: # 数字だった場合
                num = int(state)

        # 下を見る       
        if not cur_row == self.H-1:
            state = self.check(cur_row+1,cur_column)
            if state == "#":
                self.end(count)
            elif state == ".":
                self.que.append([cur_row+1,cur_column])
                self.count.append(count+1)
            elif state == "d":
                pass
            else: # 数字だった場合
                num = int(state)

        # 左を見る       
        if not cur_column == 0:
            state = self.check(cur_row,cur_column-1)
            if state == "#":
                self.end(count)
            elif state == ".":
                self.que.append([cur_row,cur_column-1])
                self.count.append(count+1)
            elif state == "d":
                pass
            else: # 数字だった場合
                num = int(state)

        # 右を見る       
        if not cur_column == self.W-1:
            state = self.check(cur_row,cur_column+1)
            if state == "#":
                self.end(count)
            elif state == ".":
                self.que.append([cur_row,cur_column+1])
                self.count.append(count+1)
            elif state == "d":
                pass
            else: # 数字だった場合
                num = int(state)

        if len(self.que) != 0 and num != -1:
            count = num + count 
            self.end(count)


    def main(self):
        while not self.terminal:
            self.bdf()  



bdf = BDF()
bdf.main()
