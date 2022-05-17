from init import *
from make_list import *
from game import *

wink=window()
bom=Bom(wink.win)
gm=game(bom)

wink.initial_start_button() #启用开始按钮
bom.make_list() #完成格子棋盘初始化
wink.initial_basic()  #完成所有初始化

gm.main_game()
    
wink.win.mainloop()  #保持窗口循环
