import customtkinter as ctk
import core.GUI.page.login as login
import core.GUI.page.setting as setting
from core.User import User as user
from core.GUI import main
from PIL import ImageFile

class GUI:
    MainWin:main.Main
    BgPic:ImageFile
    Cover:ctk.CTkToplevel
    winX=0
    winY=0
    mainTabMap={
        "登录":login.loginFrame,
        "设置":setting.settingFrame
    }
User:user