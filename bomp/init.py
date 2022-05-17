from tkinter import *
from tkinter.ttk import *
from make_list import *

class window:
    def __init__(self):
        #类内变量名
        self.win=Tk()
        self.start = PhotoImage(file = "picture\\miku_button.gif")
        self.height=600  #界面高度
        self.width=650   #界面宽度
        self.flag=0
    def initial_basic(self):
        #加载主窗口
        self.win.title("Miku Bomp")
        self.win.geometry(str(self.height)+"x"+str(self.width)+"+450+100")
        self.win.resizable(0,0)
        self.win.iconbitmap("picture/miku.ico") #加载游戏图标
        self.win["background"]="#39C5BB"
    def initial_start_button(self):
        #加载开始/重新开始图标
        self.photoimage = self.start.subsample(6,6)  #按钮大小
        st_button=Button(self.win, image = self.photoimage,command = lambda:self.initial_clear())
        st_button.place(relx=0.83,y=5)  #定位
    def initial_clear(self):
        self.flag=1
        if(self.flag==1):
            self.flag=0
            self.initial_basic()
            Bom(self.win).make_list()
            