import customtkinter as ctk

from core.GUI.widgets.ctk_toplevel_g import CTkToplevelG
from core import g_var

class moveWindow:

    # 处理鼠标按下事件
    def on_drag_start(event):
        for win in g_var.GUI.CoverWinStack[::-1]:
            win.attributes('-topmost', 'true')
        # 识别按下位置
        if str(event.widget)==".!maintabview" or str(event.widget)==".!maintabview.!ctkcanvas" or str(event.widget)==".!ctklabel.!label":
            g_var.GUI.winX=event.x
            g_var.GUI.winY=event.y

    # 处理鼠标移动事件
    def on_drag(event):
        if g_var.GUI.winY!=0:
            deltax=event.x-g_var.GUI.winX
            deltay=event.y-g_var.GUI.winY
            new_x=g_var.GUI.MainWin.winfo_x()+deltax
            new_y=g_var.GUI.MainWin.winfo_y()+deltay
            g_var.GUI.MainWin.geometry(f"+{new_x}+{new_y}")
            for win in g_var.GUI.CoverWinStack:
                win.geometry(f"+{new_x+13}+{new_y+49}")

    # 处理鼠标释放事件
    def on_drag_stop(event):
        g_var.GUI.winX=0
        g_var.GUI.winY=0
        for win in g_var.GUI.CoverWinStack:
            win.attributes('-topmost', 'false')

def up0Cover():
    g_var.GUI.CoverWinStack[0].CoverFrame.destroy()
    g_var.GUI.CoverWinStack[0].wm_attributes('-transparentcolor','#0000ff')
    g_var.GUI.CoverWinStack[0].attributes('-topmost', 'true')
    g_var.GUI.CoverWinStack[0].CoverFrame=g_var.GUI.mainTabMap[g_var.GUI.MainWin.main_tab_view.get()](g_var.GUI.CoverWinStack[0])
    g_var.GUI.CoverWinStack[0].CoverFrame.place(x=0,y=0)
    g_var.GUI.CoverWinStack[0].geometry(f"{g_var.GUI.MainWin.winfo_x()+13}+{g_var.GUI.MainWin.winfo_y()+49}")
    g_var.GUI.CoverWinStack[0].bind("<ButtonPress-1>",topWin)
    g_var.GUI.CoverWinStack[0].attributes('-topmost', 'false')

def unset0Cover():
    g_var.GUI.CoverWinStack[0].destroy()
    g_var.GUI.CoverWinStack[0]=CTkToplevelG(g_var.GUI.MainWin, fg_color="#0000ff")
    g_var.GUI.CoverWinStack[0].geometry("783x418")
    g_var.GUI.CoverWinStack[0].attributes("-alpha", 0.85)
    g_var.GUI.CoverWinStack[0].overrideredirect(True)
    g_var.GUI.CoverWinStack[0].CoverFrame=ctk.CTkFrame(g_var.GUI.CoverWinStack[0])
    up0Cover()

def topWin(arg):
    for win in g_var.GUI.CoverWinStack[::-1]:
        win.attributes('-topmost', 'true')
    g_var.GUI.MainWin.attributes('-topmost', 'true')
    g_var.GUI.MainWin.attributes('-topmost', 'false')
    for win in g_var.GUI.CoverWinStack:
        win.attributes('-topmost', 'false')

def upLoginAfter():
    g_var.GUI.MainWin.main_tab_view.delete("登录")
    g_var.GUI.MainWin.main_tab_view.delete("设置")
    g_var.GUI.MainWin.main_tab_view.add_tab("Home")
    g_var.GUI.MainWin.main_tab_view.add_tab("隧道管理")
    g_var.GUI.MainWin.main_tab_view.add_tab("设置")
    g_var.GUI.MainWin.main_tab_view.set("Home")
    g_var.User.updateTunnel()
    up0Cover()