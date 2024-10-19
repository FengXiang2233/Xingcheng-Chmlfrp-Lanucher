import customtkinter as ctk

from core import g_var

class moveWindow:

    # 处理鼠标按下事件
    def on_drag_start(event):
        g_var.GUI.Cover.attributes('-topmost', 'true')
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
            g_var.GUI.Cover.geometry(f"+{new_x+13}+{new_y+49}")

    # 处理鼠标释放事件
    def on_drag_stop(event):
        g_var.GUI.winX=0
        g_var.GUI.winY=0
        g_var.GUI.Cover.attributes('-topmost', 'false')
# TODO <优化>修改更新覆盖层更新逻辑
# 不重设覆盖层窗口 只重设Frame
def upCover():
    g_var.GUI.Cover.destroy()
    g_var.GUI.Cover=ctk.CTkToplevel(g_var.GUI.MainWin,fg_color="#0000ff")
    g_var.GUI.Cover.geometry("783x418")
    g_var.GUI.Cover.wm_attributes('-transparentcolor','#0000ff')
    g_var.GUI.Cover.attributes('-topmost', 'true')
    g_var.GUI.Cover.attributes("-alpha", 0.85)
    g_var.GUI.Cover.overrideredirect(True)
    g_var.GUI.mainTabMap[g_var.GUI.MainWin.main_tab_view.get()](g_var.GUI.Cover).place(x=0,y=0)
    g_var.GUI.Cover.geometry(f"{g_var.GUI.MainWin.winfo_x()+13}+{g_var.GUI.MainWin.winfo_y()+49}")
    g_var.GUI.Cover.bind("<ButtonPress-1>",topWin)
    g_var.GUI.Cover.attributes('-topmost', 'false')

def topWin(arg):
    g_var.GUI.Cover.attributes('-topmost', 'true')
    g_var.GUI.MainWin.attributes('-topmost', 'true')
    g_var.GUI.MainWin.attributes('-topmost', 'false')
    g_var.GUI.Cover.attributes('-topmost', 'false')

def upLoginAfter():
    g_var.GUI.MainWin.main_tab_view.delete("登录")
    g_var.GUI.MainWin.main_tab_view.delete("设置")
    g_var.GUI.MainWin.main_tab_view.add_tab("Home")
    g_var.GUI.MainWin.main_tab_view.add_tab("设置")
    g_var.GUI.MainWin.main_tab_view.add_tab("隧道管理")
    g_var.GUI.MainWin.main_tab_view.set("Home")
    g_var.User.updateTunnel()
    upCover()