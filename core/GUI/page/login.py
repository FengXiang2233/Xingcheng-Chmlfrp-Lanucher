import customtkinter as ctk
from customtkinter import CTkImage
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

        if os.path.exists("./XCL/LoginData.json") and not self.is_file_empty("./XCL/LoginData.json"):
            if os.path.isfile("./XCL/LoginData.json"):
                data=json.loads(open("./XCL/LoginData.json","r").read())
                if data["status"]:
                    token=data["token"]
            loginMain(self,token).place(x=345/2,y=148/2)
        else:
            with open("./XCL/LoginData.json", "w") as file:
                json.dump({
                    "status": False,
                    "token": None
                }, file)
            file.close()

    def is_file_empty(self, file_path):
        return os.stat(file_path).st_size == 0

    def apass(self):
        pass
# 783-438=345 418-270=148

class loginMain(ctk.CTkFrame):
    def __init__(self, master, token):
        super().__init__(master, width=438, height=270)
        ctk.CTkLabel(self, text="登 录", font=("微软雅黑", 30, "bold")).place(x=21, y=16)
        self.token = token
        self.input: loginInput = loginInput(self)
        self.input.place(x=64, y=81)
        self.login_B: ctk.CTkButton = ctk.CTkButton(
            self,
            text="登录",
            font=("微软雅黑", 15),
            width=260,
            height=32,
            command=self.userLogin
        )
        self.login_B.place(x=85, y=215)
        self.ckb_KeepLogin = ctk.CTkCheckBox(
            self,
            text="保持登录",
            font=("微软雅黑", 12.5),
            checkbox_height=16.5,
            checkbox_width=16.5
        )
        self.ckb_KeepLogin.place(x=65, y=185)
        self.tip = None

        if token is not None:
            self.login_B.configure(text="尝试登录中...", state="disabled")
            self.after(400, self.automaticLogin)

    def _update_tip(self, message, color="#ff0000"):
        if self.tip is not None:
            self.tip.destroy()
        self.tip = ctk.CTkLabel(self, text=message, font=("微软雅黑",12.6), text_color=color)
        self.tip.place(x=176,y=183)

    def automaticLogin(self):
        try:
            data = API.getUserInfo(self.token)
            if data is not None:
                data["token"] = self.token
                core.g_var.User = user(data)

                # 修改图片处理部分
                from customtkinter import CTkImage
                img = Image.open(BytesIO(requests.get(core.g_var.User.basicInfo["userimg"]).content))
                img.save("./XCL/userimg.png", 'PNG')
                ctk_img = CTkImage(light_image=img, dark_image=img, size=img.size)

                # 在切换界面之前保存当前的按钮引用
                button = self.login_B
                # 调用界面切换
                upLoginAfter()
                # 检查按钮是否还存在
                try:
                    if button.winfo_exists():
                        button.configure(text="登录", state="normal")
                except:
                    pass  # 按钮已被销毁，忽略错误
            else:
                self._update_tip("自动登录:token已失效")
                self.login_B.configure(text="登录", state="normal")
        except Exception as e:
            self._update_tip("自动登录:网络请求错误")
            self.login_B.configure(text="登录", state="normal")


    def userLogin(self):
        self.login_B.configure(text="登录中...", state="disabled")
        try:
            data = API.login(self.input.usernameEntry.get(), self.input.passwordEntey.get())
            if data is not None:
                core.g_var.User = user(data)
                Image.open(BytesIO(requests.get(core.g_var.User.basicInfo["userimg"]).content)).save("./XCL/userimg.png",'PNG')
                if self.ckb_KeepLogin.get() == 1:
                    with open("./XCL/LoginData.json","w") as file:
                        json.dump({
                            "status": True,
                            "token": data["usertoken"]
                        }, file)
                # 在切换界面之前保存当前的按钮引用
                button = self.login_B
                # 调用界面切换
                upLoginAfter()
                # 检查按钮是否还存在
                try:
                    if button.winfo_exists():
                        button.configure(text="登录", state="normal")
                except:
                    pass  # 按钮已被销毁，忽略错误
            else:
                self._update_tip("账号密码错误")
                self.login_B.configure(text="登录", state="normal")
        except:
            self._update_tip("网络请求错误")
            self.login_B.configure(text="登录", state="normal")

class loginInput(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        ctk.CTkLabel(self,text="用户名：",font=("微软雅黑",16.5)).grid(row=0,column=0)
        ctk.CTkLabel(self,text="密   码：",font=("微软雅黑",16.5)).grid(row=1,column=0)
        self.usernameEntry:ctk.CTkEntry=ctk.CTkEntry(self,width=225,placeholder_text="你tm倒是填a")
        self.usernameEntry.grid(row=0,column=1,pady=11,padx=5.5)
        self.passwordEntey:ctk.CTkEntry=ctk.CTkEntry(self,width=225,placeholder_text="你tm倒是填a")
        self.passwordEntey.grid(row=1,column=1,pady=11,padx=5.5)
