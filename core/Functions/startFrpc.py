from typing import Union

import core.g_var
import os

def startFrpc(tun_id:Union[str,int]):
    with open("./XCL/LatestLaunch.bat","w") as file:
        file.write(f"@echo off\n.\\res\\frpc.exe -u {core.g_var.User.token} -p {tun_id}\npause\nexit")
    os.system(f"start \"frpc-{tun_id}\" .\XCL\LatestLaunch.bat")