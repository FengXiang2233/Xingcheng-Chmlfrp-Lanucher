import customtkinter as ctk

class loginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        loginMain(self).place(x=(783-443)/2,y=(418-286)/2)

class loginMain(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=438,height=270)
        ctk.CTkLabel(self,text="登 录",font=("微软雅黑",30,"bold")).place(x=21,y=16)
        self.input=loginInput(self).place(x=64,y=81)
        ctk.CTkButton(self,text="登录",font=("微软雅黑",15),width=260,height=32).place(x=85,y=215)
        ctk.CTkCheckBox(self,text="保持登录",font=("微软雅黑",12.5),checkbox_height=16.5,checkbox_width=16.5).place(x=65,y=185)

class loginInput(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        ctk.CTkLabel(self,text="用户名：",font=("微软雅黑",16.5)).grid(row=0,column=0)
        ctk.CTkLabel(self,text="密   码：",font=("微软雅黑",16.5)).grid(row=1,column=0)
        self.usernameEntry=ctk.CTkEntry(self,width=225,placeholder_text="这里是用户名").grid(row=0,column=1,pady=11,padx=5.5)
        self.passwordEntey=ctk.CTkEntry(self,width=225,placeholder_text="这里是密码").grid(row=1,column=1,pady=11,padx=5.5)
