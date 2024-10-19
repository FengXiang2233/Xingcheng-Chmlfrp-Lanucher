from core.network import chmlfrp_APIv2

cfAPI=chmlfrp_APIv2.APIv2

class User:
    TunnelDict:dict={}
    def __init__(self,loginData:dict):
        self.token=loginData["usertoken"]
        self.id=loginData["id"]
        self.basicInfo=loginData

    def updateTunnel(self):
        data=cfAPI.getUserTunnelList(self.token)
        if data is None:
            return False
        else:
            self.TunnelDict=data
            return True