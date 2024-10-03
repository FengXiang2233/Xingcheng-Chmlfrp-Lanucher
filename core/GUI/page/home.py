import customtkinter as ctk
import core.g_var

from core.network.chmlfrp_APIv2 import APIv2 as API

class loginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        