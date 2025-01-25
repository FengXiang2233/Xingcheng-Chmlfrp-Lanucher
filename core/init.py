import os
import logging
import customtkinter as ctk
import json

from core import g_var
from PIL import Image


def init():
    # 登录
    open("./last.log", "w").close()
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(funcName)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(filename="./last.log", encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    # Lanucher 初始化
    logging.info("程序初始化中..")
    LanucherInit()

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

def LanucherInit():
    # XCL dir
    if not os.path.isdir("./XCL"):
        os.mkdir("./XCL")
        logging.debug("XCL目录不存在 已自动创建")

    # bg
    if not os.path.isfile("./XCL/bg.jpg"):
        Image.new(mode='RGB', size=(810, 450), color=(201, 221, 244)).save("./XCL/bg.jpg")
        logging.debug("背景图片不存在 已自动创建")

    # theme
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("./res/xcTheme.json")

    # 使用 CTkImage 替代直接的 PIL Image
    bg_pil = Image.open("./XCL/bg.jpg")
    g_var.GUI.BgPic = ctk.CTkImage(
        light_image=bg_pil,
        dark_image=bg_pil,  # 如果需要，可以为暗色主题设置不同的图片
        size=(810, 450)
    )