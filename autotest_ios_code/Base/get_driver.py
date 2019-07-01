# -*- coding: UTF-8 -*-
from appium import webdriver

def get_driver():
                # server 启动参数
    desired_caps = {
                "platformName": "Android",
                "platformVersion": "8.0",
                "deviceName": "192.168.56.101:5555",
                "appPackage": "com.comiatrogenic.qaj",
                "appActivity": "com.uzmap.pkg.EntranceActivity",
                "unicodeKeyboard": True,
                "resetKeyboard": True
            }    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
