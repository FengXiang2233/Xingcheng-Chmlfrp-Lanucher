import customtkinter as ctk

import core.g_var
from core.GUI.widgets import CTkScrollableFrameFrame

class upMenuButton(ctk.CTkFrame):
    def __init__(self,master:ctk.CTkFrame,text:str,Menu:list):
        super().__init__(master,fg_color="#0000ff")
        self.menu=Menu
        self.text=text
        self.menuStatus=False
        self.menuObj:MenuFrame=None
        self.master:ctk.CTkFrame=master
        self.mainButton:ctk.CTkButton=ctk.CTkButton(self,text=self.text,height=43,corner_radius=0,state=False)
        self.menuButton:ctk.CTkButton=ctk.CTkButton(self,text="⇧",font=("微软雅黑",20,"bold"),height=43,width=15,border_width=1.5,border_color="gray90",corner_radius=0,command=self.menuOperation)
        self.mainButton.pack(side="left")
        self.menuButton.pack(side="left")
    def menuOperation(self):
        if self.menuStatus:
            self.menuObj.destroy()
            self.menuStatus=False
            self.menuButton.configure(text="⇧")
        else:
            self.menuObj=MenuFrame(self,self.menu)
            self.menuObj.place(x=self.winfo_x(),y=self.winfo_y()-210)
            self.menuStatus=True
            self.menuButton.configure(text="⇩")

# TODO 选择后关闭菜单
class MenuFrame(CTkScrollableFrameFrame.CTkScrollableFrameFrame):
    def __init__(self,master:ctk.CTkFrame,Menu:list):
        super().__init__(core.g_var.GUI.Cover,width=142)
        for options in Menu:
            Options(self.ScrollableFrame,options).pack(anchor=ctk.W)

class Options(ctk.CTkButton):
    def __init__(self,master,text:str):
        super().__init__(master,text=text)