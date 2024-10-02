import logging
import requests

class APIv2:
    url="https://cf-v2.uapis.cn"
    def login(username:str,password:str):
        data=requests.get(APIv2.url+"/login",{
            "username":username,
            "password":password
        }).json()
        if data["code"]==200:
            return data["data"]
        else:
            return None