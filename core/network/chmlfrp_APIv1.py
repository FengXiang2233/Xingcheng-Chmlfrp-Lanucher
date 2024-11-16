import requests

class APIv1:
    url="https://cf-v1.uapis.cn"
    def reToken(usertoken:str)->str:
        data:dict=requests.get(APIv1.url+"/userinfo",{
            "token":usertoken
        }).json()
        if "newToken" in data.keys():
            return data["newToken"]
        else:
            return None