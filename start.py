from core import init,g_var
from core.GUI import main
import os
import json

init.init()
def start():
    # 启动！
    g_var.GUI.MainWin=main.Main()
    g_var.GUI.MainWin.mainloop()

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

if __name__ == '__main__':
    if os.path.exists("./XCL/LoginData.json") and not is_file_empty("./XCL/LoginData.json"):
        start()
    else:
        restoration()
        start()
