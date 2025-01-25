from core import init,g_var
from core.GUI import main
import os


def start():
    # 启动！
    g_var.GUI.MainWin = main.Main()
    g_var.GUI.MainWin.mainloop()


# -----启动程序------
if __name__ == '__main__':
    init.init()
    if os.path.exists("./XCL/LoginData.json") and not init.is_file_empty("./XCL/LoginData.json"):
        start()
    else:
        # 配置文件检查防止崩溃
        init.detection()
        # 补全文件后启动
        start()