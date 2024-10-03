import customtkinter as ctk

class settingFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        settingMain(self).place(x=(783-438)/2,y=(418-270)/2)

class settingMain(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=438,height=270)
        self.pack_propagate(0)
        ctk.CTkLabel(self,text="还没写",font=("微软雅黑",30)).pack(pady=15)
        ctk.CTkLabel(self,text="咕咕咕",font=("微软雅黑",50,"bold")).pack()