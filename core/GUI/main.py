import customtkinter as ctk
import sys
from win32gui import FindWindow, GetWindowLong, SetWindowLong, SetWindowPos, GetForegroundWindow
from win32con import GWL_EXSTYLE, WS_EX_APPWINDOW, HWND_NOTOPMOST, SWP_NOMOVE, SWP_NOSIZE, SWP_FRAMECHANGED

from core.GUI.widgets.ctk_button_g import CTkButtonG
from core.GUI.mainTabView import MainTabView
from core.GUI import windowManager
from core import g_var


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("XingCheng Chmlfrp Lanucher - main")
        self.geometry("810x480")
        self.wm_attributes('-transparentcolor', '#0000ff')
        self.overrideredirect(True)
        self.main_tab_view = MainTabView(master=self)
        self.main_tab_view.place(x=0, y=0)
        self.close_win_button = CTkButtonG(
            self,
            text="x",
            width=42,
            height=42,
            font=("微软雅黑", 23, "bold"),
            corner_radius=15,
            command=self.destroy,
            fg_color="#ebebeb",
            hover_color="#e1e1e1",
            text_color="#bebebe"
        )
        self.close_win_button.place(relx=0.92, y=5)
        ctk.CTkLabel(self, text="XCL  II", font=("微软雅黑", 22, "bold")).place(x=30, y=10)

        # 遮盖背景
        self.shelter_down = ctk.CTkLabel(self, text="", width=810, height=13, bg_color="#0000FF")
        self.shelter_down.place(x=0, y=467)
        self.shelter_left = ctk.CTkLabel(self, text="", width=13, height=480, bg_color="#0000FF")
        self.shelter_left.place(x=0, y=0)
        self.shelter_right = ctk.CTkLabel(self, text="", width=13, height=480, bg_color="#0000FF")
        self.shelter_right.place(x=797, y=0)

        self.bind("<ButtonPress-1>", windowManager.moveWindow.on_drag_start)
        self.bind("<B1-Motion>", windowManager.moveWindow.on_drag)
        self.bind("<ButtonRelease-1>", windowManager.moveWindow.on_drag_stop)

        # Login 窗口处理
        self.main_tab_view.add_tab("登录")
        self.main_tab_view.add_tab("设置")

        self.update_idletasks()
        self.hwnd = FindWindow(None, self.title())
        self.add_taskbar_icon()
        self.attributes('-topmost', 'true')
        self.attributes('-topmost', 'false')

    def mainloop(self, *args, **kwargs):
        g_var.GUI.Cover = ctk.CTkToplevel(g_var.GUI.MainWin)
        windowManager.unsetCover()
        self.check_topmost()
        super().mainloop(*args, **kwargs)

    def check_topmost(self):
        try:
            top_window = GetForegroundWindow()
            if top_window == self.hwnd:
                g_var.GUI.Cover.attributes('-topmost', 'true')
                g_var.GUI.Cover.attributes('-topmost', 'false')
        except Exception:
            pass
        self.after(50, self.check_topmost)

    def add_taskbar_icon(self):
        # 修改窗口样式，WS_EX_APPWINDOW 确保窗口在任务栏中显示
        extended_style = GetWindowLong(self.hwnd, GWL_EXSTYLE)
        SetWindowLong(self.hwnd, GWL_EXSTYLE, extended_style | WS_EX_APPWINDOW)
        SetWindowPos(
            self.hwnd,
            HWND_NOTOPMOST,
            0, 0, 0, 0,
            SWP_NOMOVE | SWP_NOSIZE | SWP_FRAMECHANGED
        )