import customtkinter as ctk

class CTkScrollableFrameFrame(ctk.CTkFrame):
    def __init__(self,master,
                 width: int = 200,
                 height: int = 200,):
        super().__init__(master,width,height)
        self.ScrollableFrame:ctk.CTkScrollableFrame=ctk.CTkScrollableFrame(self,width,height)
        self.ScrollableFrame.pack()