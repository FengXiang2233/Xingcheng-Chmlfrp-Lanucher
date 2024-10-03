import customtkinter as ctk

import core.g_var
from core.User import User as user
from core.GUI.windowManager import upLoginAfter
from core.network.chmlfrp_APIv2 import APIv2 as API

class loginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        loginMain(self).place(x=(783-438)/2,y=(418-270)/2)

class loginMain(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=438,height=270)
        ctk.CTkLabel(self,text="登 录",font=("微软雅黑",30,"bold")).place(x=21,y=16)
        self.input:loginInput=loginInput(self)
        self.input.place(x=64,y=81)
        self.login_B:ctk.CTkButton=ctk.CTkButton(self,text="登录",font=("微软雅黑",15),width=260,height=32,command=self.login)
        self.login_B.place(x=85,y=215)
        self.ckb_KeepLogin=ctk.CTkCheckBox(self,text="保持登录",font=("微软雅黑",12.5),checkbox_height=16.5,checkbox_width=16.5)
        self.ckb_KeepLogin.place(x=65,y=185)
        self.tip:ctk.CTkLabel
    def login(self):
        self.tip:ctk.CTkLabel=ctk.CTkLabel(self,text="账号密码错误",font=("微软雅黑",12.6),text_color="#ff0000")
        self.tip.place(x=176,y=183)
        self.tip.destroy()
        self.login_B.configure(text="登录中...",state="disabled")
        data=API.login(self.input.usernameEntry.get(),self.input.passwordEntey.get())
        if data is not None:
            core.g_var.User=user(data)
            upLoginAfter()
        else:
            self.tip:ctk.CTkLabel=ctk.CTkLabel(self,text="账号密码错误",font=("微软雅黑",12.6),text_color="#ff0000")
            self.tip.place(x=176,y=183)
            self.login_B.configure(text="登录",state="normal")

class loginInput(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        ctk.CTkLabel(self,text="用户名：",font=("微软雅黑",16.5)).grid(row=0,column=0)
        ctk.CTkLabel(self,text="密   码：",font=("微软雅黑",16.5)).grid(row=1,column=0)
        self.usernameEntry:ctk.CTkEntry=ctk.CTkEntry(self,width=225,placeholder_text="你tm倒是填a")
        self.usernameEntry.grid(row=0,column=1,pady=11,padx=5.5)
        self.passwordEntey:ctk.CTkEntry=ctk.CTkEntry(self,width=225,placeholder_text="你tm倒是填a")
        self.passwordEntey.grid(row=1,column=1,pady=11,padx=5.5)
