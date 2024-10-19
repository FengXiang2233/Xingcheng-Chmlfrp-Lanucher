import customtkinter as ctk

class panelBButton(ctk.CTkButton):
    def __init__(self,master,**kwargs):
        super().__init__(master,fg_color="#e5e5ec",hover_color="#e2e2e9",border_width=1,border_color="#409eff",text_color="#409eff",**kwargs)

class panelRButton(ctk.CTkButton):
    def __init__(self,master,**kwargs):
        super().__init__(master,fg_color="#ece5e5",hover_color="#e9e2e2",border_width=1,border_color="#f56c6c",text_color="#f56c6c",**kwargs)