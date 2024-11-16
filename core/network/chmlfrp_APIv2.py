import requests

class APIv2:
    url="https://cf-v2.uapis.cn"
    def login(username:str,password:str)->dict:
        data=requests.get(APIv2.url+"/login",{
            "username":username,
            "password":password
        }).json()
        if data["code"]==200:
            return data["data"]
        else:
            return None
    def getUserTunnelList(usertoken:str)->dict:
        data=requests.get(APIv2.url+"/tunnel",{
            "token":usertoken
        }).json()
        if data["code"]==200:
            redata={}
            for i in data["data"]:
                redata[i["id"]]=i
            return redata
        else:
            return None
    def getUserInfo(usertoken:str)->dict:
        data=requests.get(APIv2.url+"/userinfo",{
            "token":usertoken
        }).json()
        if data["code"]==200:
            return data["data"]
        else:
            return None