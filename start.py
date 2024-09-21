from core import init,g_var
from core.GUI import main

init.init()
# 启动！
g_var.GUI.MainWin=main.Main()
g_var.GUI.MainWin.mainloop()
