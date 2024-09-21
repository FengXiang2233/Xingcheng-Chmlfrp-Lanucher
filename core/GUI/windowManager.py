import customtkinter as ctk

from core import g_var

class moveWindow:

    # 处理鼠标按下事件
    def on_drag_start(event):
        # 识别按下位置
        if str(event.widget)==".!maintabview" or str(event.widget)==".!maintabview.!ctkcanvas":
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
            g_var.GUI.Cover.geometry(f"+{new_x+14}+{new_y+49}")

    # 处理鼠标释放事件
    def on_drag_stop(event):
        g_var.GUI.winX=0
        g_var.GUI.winY=0

def upCover():
    g_var.GUI.Cover.destroy()
    g_var.GUI.Cover=ctk.CTkToplevel(g_var.GUI.MainWin,fg_color="#0000ff")
    g_var.GUI.Cover.geometry("783x418")
    g_var.GUI.Cover.wm_attributes('-transparentcolor','#0000ff')
    g_var.GUI.Cover.attributes('-topmost', 'true')
    g_var.GUI.Cover.attributes("-alpha", 0.7)
    g_var.GUI.Cover.overrideredirect(True)
    g_var.GUI.mainTabMap[g_var.GUI.mainTab](g_var.GUI.Cover).place(x=0,y=0)
    g_var.GUI.Cover.geometry(f"{g_var.GUI.MainWin.winfo_x()+14}+{g_var.GUI.MainWin.winfo_y()+49}")
    