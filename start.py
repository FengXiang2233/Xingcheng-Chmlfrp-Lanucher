from core import init,g_var
from core.GUI import main
import os
import json

init.init()
# -----启动函数------
def start():
    # 启动！
    g_var.GUI.MainWin=main.Main()
    g_var.GUI.MainWin.mainloop()

# -----配置文件检查防止崩溃------
def is_file_empty(file_path):
    return os.stat(file_path).st_size == 0

def restoration():
    with open("./XCL/LoginData.json", "w") as file:
        json.dump({
            "status": False,
            "token": None
        }, file)
    file.close()

def detection():
    try:
        data = json.loads(open("./XCL/LoginData.json", "r").read())
        a = data["status"]
        b = data["token"]
        data.close()
        if a == "":
            restoration()
        if b == "":
            restoration()
    except:
        restoration()

# -----启动程序------

if __name__ == '__main__':
    if os.path.exists("./XCL/LoginData.json") and not is_file_empty("./XCL/LoginData.json"):
        start()
    else:
        restoration()
        start()
