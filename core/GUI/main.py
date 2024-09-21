import customtkinter as ctk
import sys
import win32gui,win32con
import ctypes

from core.GUI.mainTabView import MainTabView
from core.GUI import windowManager
from core import g_var

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("XingCheng Chmlfrp Lanucher - main")
        self.geometry("810x480")
        self.wm_attributes('-transparentcolor','#0000ff')
        self.overrideredirect(True)
        # 主窗口切换界面
        self.main_tab_view=MainTabView(master=self)
        self.main_tab_view.place(x=0,y=0)
        # 关闭窗口按钮
        self.close_win_button=ctk.CTkButton(self,text="x",width=27,height=27,font=("Arial",23,"bold"),corner_radius=24,command=self.close_win,fg_color="#ebebeb",hover_color="#e1e1e1",text_color="#bebebe")
        self.close_win_button.place(relx=0.92,y=5)
        # 遮盖背景
        self.shelter_down=ctk.CTkLabel(self,text="",width=810,height=13,bg_color="#0000FF")
        self.shelter_down.place(x=0,y=467)
        self.shelter_left=ctk.CTkLabel(self,text="",width=13,height=480,bg_color="#0000FF")
        self.shelter_left.place(x=0,y=0)
        self.shelter_right=ctk.CTkLabel(self,text="",width=13,height=480,bg_color="#0000FF")
        self.shelter_right.place(x=797,y=0)
        self.bind("<ButtonPress-1>",windowManager.moveWindow.on_drag_start)
        self.bind("<B1-Motion>",windowManager.moveWindow.on_drag)
        self.bind("<ButtonRelease-1>",windowManager.moveWindow.on_drag_stop)
        # Login 窗口处理
        self.main_tab_view.add_tab("登录")
        self.main_tab_view.add_tab("设置")
        # -
        self.update_idletasks()
        self.hwnd=win32gui.FindWindow(None, self.title())
        self.add_taskbar_icon()

    # Override
    def mainloop(self, *args, **kwargs):
        if not self._window_exists:
            if sys.platform.startswith("win"):
                self._windows_set_titlebar_color(self._get_appearance_mode())

                if not self._withdraw_called_before_window_exists and not self._iconify_called_before_window_exists:
                    self.deiconify()

            self._window_exists = True
        g_var.GUI.Cover=ctk.CTkToplevel(g_var.GUI.MainWin)
        windowManager.upCover()
        self.check_topmost()
        super().mainloop(*args, **kwargs)

    # 关闭窗口
    def close_win(self):
        self.destroy()

    def check_topmost(self):
        # 获取当前最上面的窗口句柄
        top_window = win32gui.GetForegroundWindow()
        if top_window == self.hwnd:
            g_var.GUI.Cover.attributes('-topmost', 'true')
            g_var.GUI.Cover.attributes('-topmost', 'false')
        # 继续循环检查
        self.after(75, self.check_topmost)
    
    # 保留任务栏图标
    def add_taskbar_icon(self):
        # 修改窗口样式，WS_EX_APPWINDOW 确保窗口在任务栏中显示
        extended_style = win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, extended_style | win32con.WS_EX_APPWINDOW)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)