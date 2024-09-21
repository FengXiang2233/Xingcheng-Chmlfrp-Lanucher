import customtkinter as ctk

class loginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        ctk.CTkButton(self,text="北风酱~").place(x=0,y=0)