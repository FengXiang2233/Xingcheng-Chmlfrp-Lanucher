import customtkinter as ctk
import win32clipboard

from core.GUI.widgets.ctk_button_g import CTkButtonG
from core.GUI.widgets.panelButton import panelBButton,panelRButton
from core.GUI.widgets.tip_cover import TipCover
from core.Functions.startFrpc import startFrpc
import core.g_var
from core.network.chmlfrp_APIv1 import APIv1
import time

class tunnelManagerFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        self.after(5000,core.g_var.User.updateTunnel)
        tunnelManagerMain(self).pack()

class tunnelManagerMain(ctk.CTkScrollableFrame):
    def __init__(self,master):
        super().__init__(master,width=769,height=418,corner_radius=0,fg_color="#0000ff",scrollbar_button_color="gray65",scrollbar_button_hover_color="gray60")
        self.add_tun_card=ctk.CTkButton(self,text="+",font=("微软雅黑",60),fg_color="#e9e9e9",hover_color="#e5e5e5",text_color="#c3c3c3",width=245,height=183,corner_radius=12)
        self.add_tun_card.grid(row=0,column=0,pady=7,padx=6)
        self.after(100,self.build)

    def build(self):
        # 先清除所有现有的隧道卡片（除了添加按钮）
        for widget in self.winfo_children():
            if isinstance(widget, tunnelCard):
                widget.destroy()

        self.add_tun_card.grid(row=0, column=0, pady=7, padx=6)

        k = 1
        for i in core.g_var.User.TunnelDict:
            tunnelCard(self, core.g_var.User.TunnelDict[i]).grid(row=int(k / 3), column=int(k % 3), pady=7, padx=6)
            k += 1

class tunnelCard(ctk.CTkFrame):
    def __init__(self,master,info:dict):
        super().__init__(master,fg_color="#e5e5e5",width=245,height=183,corner_radius=12)

        self.tun_id=info["id"]

        ctk.CTkLabel(self,text=f"#{self.tun_id}",font=("微软雅黑",15.5)).place(x=13,y=7)
        ctk.CTkLabel(self,text=info["name"],font=("微软雅黑",15.5,"bold")).place(x=(len(str(info["id"]))+2)*9+12,y=7)
        ctk.CTkLabel(self,text="内网地址: "+info["localip"]+":"+str(info["nport"])+" - "+info["type"],font=("微软雅黑",13)).place(x=13,y=37)
        ctk.CTkLabel(self,text="节点信息: "+info["node"],font=("微软雅黑",13)).place(x=13,y=57)
        try:
            if info["type"] in ["http",'https']:
                self.cUrl=info["dorp"]
            else:
                self.cUrl=info["ip"]+":"+info["dorp"]
        except:
            self.cUrl=""
        cUrlLabel=ctk.CTkLabel(self,text="连接地址: "+self.cUrl,font=("微软雅黑",13))
        cUrlLabel.bind("<ButtonPress-1>",self.copyUrl)
        cUrlLabel.place(x=13,y=77)
        self.tip:TipCover=TipCover(self,cUrlLabel,text="点击以复制")
        panelBButton(self,text="启动隧道",width=219,command=self.startFrp).place(x=13,y=108)
        panelRButton(self,text="删除隧道",width=219,command=self.tunnel_deletionv1).place(x=13,y=143)

    def startFrp(self):
        startFrpc(self.tun_id)

    def tunnel_deletionv1(self):
        # TODO: 删除最后一个隧道时ui好像无法删除
        if APIv1.tunnel_deletion(core.g_var.User.token, core.g_var.User.id, self.tun_id):
            core.g_var.User.updateTunnel()
            time.sleep(0.5)
            self.master.build()
        else:
            self.master.build()
            ctk.CTkMessageBox.show_error("删除失败", "请检查您的网络连接")


    def copyUrl(self,arg):
        self.tip.ctext("已复制")
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,self.cUrl)
        win32clipboard.CloseClipboard()