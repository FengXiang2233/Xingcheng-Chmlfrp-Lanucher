from typing import Union

import core.g_var
import os

def startFrpc(tun_id:Union[str,int]):
    os.system(f'start \"frpc - {tun_id}\" cmd /k \"{os.getcwd()}/res/frpc.exe -u {core.g_var.User.token} -p {tun_id}\"')