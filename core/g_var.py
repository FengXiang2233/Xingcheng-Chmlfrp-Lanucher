import customtkinter as ctk
from core.GUI import main
from core.GUI.page import login
from PIL import ImageFile

class GUI:
    MainWin:main.Main
    BgPic:ImageFile
    Cover:ctk.CTkToplevel
    mainTab:str="登录"
    winX=0
    winY=0
    mainTabMap={
        "登录":login.loginFrame
    }