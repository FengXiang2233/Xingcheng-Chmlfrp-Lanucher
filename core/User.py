from core.network import chmlfrp_APIv2

cfAPI=chmlfrp_APIv2.APIv2

class User:

    def __init__(self,loginData:dict):
        self.token=loginData["usertoken"]
        self.id=loginData["id"]
        self.basicInfo=loginData
    