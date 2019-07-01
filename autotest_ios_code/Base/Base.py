# -*- coding: UTF-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
import os

class Base:
    def __init__(self,driver):
        self.driver = driver

    def search_element(self,loc, timeout=15):
        # 定位单个元素

        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))

    def search_elements(self,loc, timeout=15):
        # 定位多个元素

        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout= 15):
        # 点击元素
        self.search_element(loc, timeout).click()

    def input_element(self,loc,text_value, timeout=20):
        # 输入内容
        input_text = self.search_element(loc,timeout)
        input_text.clear()
        input_text.send_keys(text_value)

    def swipe_Up(self, n=1, timeout=15):
        L = self.driver.get_window_size()
        x1 = L['width'] * 0.5
        y1 = L['height'] * 0.75
        y2 = L['height'] * 0.25
        for i in range(n,timeout):
            self.driver.swipe(x1, y1, x1, y2, 100)

    # 屏幕向下滑动, x轴不变，y轴向上移动
    def swipe_Down(self, n=1,timeout=15):
        L = self.driver.get_window_size()
        x1 = L['width'] * 0.5
        y1 = L['height'] * 0.25
        y2 = L['height'] * 0.75
        for i in range(n,timeout):
            self.driver.swipe(x1, y2, x1, y1, 100)

    #屏幕截图
    def jie_tu(self):
        self.driver.get_screenshot_as_file(os.getcwd()+os.sep+'./screen.png')





