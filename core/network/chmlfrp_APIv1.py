import requests

class APIv1:
    url="https://cf-v1.uapis.cn/api"

    def reToken(usertoken:str)->str:
        data:dict=requests.get(APIv1.url+"/userinfo",{
            "token":usertoken
        }).json()
        if "newToken" in data.keys():
            return data["newToken"]
        else:
            return None

    def tunnel_deletion(usertoken:str,userid:int,nodeid:int):
        url_v1 = f"{APIv1.url}/deletetl.php"
        params = {
            "token": usertoken,
            "userid": userid,
            "nodeid": nodeid,
        }
        response_v1 = requests.get(url_v1, params=params)
        if response_v1.status_code == 200:
            return True
        else:
            return False