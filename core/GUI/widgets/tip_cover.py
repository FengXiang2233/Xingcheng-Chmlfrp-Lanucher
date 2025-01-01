import customtkinter as ctk

class TipCover:
    def __init__(self, master,smaster:ctk.CTkFrame,**kwargs):
        self.kwargs=kwargs
        self.master=master
        self.smaster:ctk.CTkFrame=smaster
        smaster.bind("<Enter>",command=self.setUpTip,add="+")
        smaster.bind("<Leave>",command=self.dTip,add="+")
    def setUpTip(self,event):
        self.tl:ctk.CTkLabel=ctk.CTkLabel(self.master,height=0,font=("微软雅黑",13),text_color="#686868",fg_color="gray95",**self.kwargs)
        self.smaster.bind("<Motion>",command=self.movetl,add="+")
    def dTip(self,event):
        self.smaster.unbind("<Motion>")
        self.tl.destroy()
    def ctext(self,ctext):
        self.tl.configure(text=ctext)
    def movetl(self,event):
        self.tl.place(x=event.x,y=event.y+52)