from tkinter import *
import random
from matplotlib.pyplot import text
#from tkinter.ttk import *

class Bom:
    def __init__(self,win):
        self.win=win
        self.size=20  #按钮大小
        self.start_y=30  
        self.start_x=30  #定位起始位置（待优化）
        self.nums_row=20
        self.nums_col=20 #格子个数
        self.lst=[]
        self.flag=[]
        self.bomb=[]
        self.bomb_num=50 #雷的个数
    
    def make_bomb(self):
        for i in range(self.bomb_num):
            self.bomb.append(random.randint(0,(len(self.lst)-1)))

    def make_list(self):
        """生成雷与空格的棋盘"""
        x_step=(self.nums_col+1)*self.size
        y_step=(self.nums_row+1)*self.size #计算range内的数值大小
        for i in range(self.start_x,x_step,self.size):
            for j in range (self.start_y,y_step,self.size):
                self.lst.append([i,j]) #生成可用列表
        self.make_bomb()
        for k in self.lst:
            bt=Button(self.win,bg="#778899",command=lambda arg=k :self.return_flag(arg)) #生成格子
            bt.place(x=k[0],y=k[1],width=self.size,height=self.size)
        
    def return_flag(self,flag):
        self.flag=flag
        #print(self.flag,len(self.flag))
        self.bomb_maker()

    def bomb_maker(self):
        flag=self.flag
        #print(flag)
        #print(self.bomb,self.lst,self.flag,len(self.lst),sep="\n")
        if self.lst.index(flag) in self.bomb:
            bt=Label(self.win,bg="#000000")
            if len(flag)!=0:        
                bt.place(x=flag[0],y=flag[1],width=self.size,\
                    height=self.size) #点击后更新格子变化
        else:
            bt=Label(self.win,bg="#FFFFFF")
            if len(flag)!=0:        
                bt.place(x=flag[0],y=flag[1],width=self.size,\
                    height=self.size) #点击后更新格子变化
