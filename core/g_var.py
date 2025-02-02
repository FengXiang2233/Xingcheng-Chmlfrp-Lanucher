import customtkinter as ctk
import core.GUI.page.home as home
import core.GUI.page.login as login
import core.GUI.page.setting as setting
import core.GUI.page.tunnelManager as tunnelManager
from core.User import User as user
from core.GUI import main
from core.GUI.widgets.ctk_toplevel_g import CTkToplevelG
from PIL import ImageFile
from typing import List

class GUI:
    MainWin:main.Main
    BgPic:ImageFile
    CoverWinStack:List[CTkToplevelG]=[]
    winX=0
    winY=0
    mainTabMap={
        "登录":login.loginFrame,
        "设置":setting.settingFrame,
        "Home":home.homeFrame,
        "隧道管理":tunnelManager.tunnelManagerFrame
    }
User:user