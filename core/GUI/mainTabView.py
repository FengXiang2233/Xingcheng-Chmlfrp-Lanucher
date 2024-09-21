import customtkinter as ctk

from core import g_var
from PIL import ImageTk
from core import g_var
from core.GUI import windowManager

class MainTabView(ctk.CTkTabview):
    def __init__(self,master):
        super().__init__(master,height=480,width=810,corner_radius=13,fg_color="#ebebeb",segmented_button_fg_color="#ebebeb",segmented_button_selected_color="#d7d7d7",segmented_button_unselected_hover_color="#d7d7d7",segmented_button_selected_hover_color="#d7d7d7",segmented_button_unselected_color="#ebebeb",text_color="#969696")
    
    # Override
    def _segmented_button_callback(self, selected_name):
        self._tab_dict[self._current_name].grid_forget()
        self._current_name = selected_name
        self._set_grid_current_tab()
        g_var.GUI.mainTab=selected_name
        windowManager.upCover()
        if self._command is not None:
            self._command()

    def add_tab(self,name:str):
        self.add(name)
        ctk.CTkLabel(self.tab(name),text="",image=ImageTk.PhotoImage(g_var.GUI.BgPic)).place(x=0,y=0)