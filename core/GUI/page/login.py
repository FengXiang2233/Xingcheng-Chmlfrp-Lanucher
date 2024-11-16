import customtkinter as ctk
import requests
import json
import os.path

import core.g_var
from io import BytesIO
from PIL import Image
from core.User import User as user
from core.GUI.windowManager import upLoginAfter
from core.network.chmlfrp_APIv2 import APIv2 as API

class loginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        token=None
        if os.path.isfile("./XCL/LoginData.json"):
            data=json.loads(open("./XCL/LoginData.json","r").read())
            if data["status"]:
                token=data["token"]
        loginMain(self,token).place(x=345/2,y=148/2)
# 783-438=345 418-270=148

class loginMain(ctk.CTkFrame):
    def __init__(self,master,token):
        super().__init__(master,width=438,height=270)
        ctk.CTkLabel(self,text="登 录",font=("微软雅黑",30,"bold")).place(x=21,y=16)
        self.token=token
        self.input:loginInput=loginInput(self)
        self.input.place(x=64,y=81)
        self.login_B:ctk.CTkButton=ctk.CTkButton(self,text="登录",font=("微软雅黑",15),width=260,height=32,command=self.userLogin)
        self.login_B.place(x=85,y=215)
        self.ckb_KeepLogin=ctk.CTkCheckBox(self,text="保持登录",font=("微软雅黑",12.5),checkbox_height=16.5,checkbox_width=16.5)
        self.ckb_KeepLogin.place(x=65,y=185)
        if token is not None:
            self.login_B.configure(text="尝试登录中...",state="disabled")
            self.after(300,self.automaticLogin)

    def automaticLogin(self):
        try:
            data=API.getUserInfo(self.token)
            # TODO 自动下载frpc
            if data is not None:
                data["token"]=self.token
                core.g_var.User=user(data)
                Image.open(BytesIO(requests.get(core.g_var.User.basicInfo["userimg"]).content)).save("./XCL/userimg.png",'PNG')
                upLoginAfter()
            else:
                self.tip:ctk.CTkLabel=ctk.CTkLabel(self,text="自动登录:token已失效",font=("微软雅黑",12.6),text_color="#ff0000")
        except:
            self.tip:ctk.CTkLabel=ctk.CTkLabel(self,text="自动登录:网络请求错误",font=("微软雅黑",12.6),text_color="#ff0000") 
        self.tip.place(x=176,y=183)
        self.login_B.configure(text="登录",state="normal")

    def userLogin(self):
        self.login_B.configure(text="登录中...",state="disabled")
        try:
            data=API.login(self.input.usernameEntry.get(),self.input.passwordEntey.get())
            # TODO 自动下载frpc
            if data is not None:
                core.g_var.User=user(data)
                Image.open(BytesIO(requests.get(core.g_var.User.basicInfo["userimg"]).content)).save("./XCL/userimg.png",'PNG')
                if self.ckb_KeepLogin.get()==1:
                    with open("./XCL/LoginData.json","w") as file:
                        file.write(json.dumps({
                            "status":True,
                            "token":data["usertoken"]
                        }))
                        file.close()
                upLoginAfter()
            else:
                self.tip:ctk.CTkLabel=ctk.CTkLabel(self,text="账号密码错误",font=("微软雅黑",12.6),text_color="#ff0000")
        except:
            self.tip:ctk.CTkLabel=ctk.CTkLabel(self,text="网络请求错误",font=("微软雅黑",12.6),text_color="#ff0000")
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
