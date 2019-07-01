# -*- coding: UTF-8 -*-
from Page.login_page import Login_page
from Page.home_page import Home_page
"""
    统一入口类
"""

class Page:

    def __init__(self, driver):
        self.driver = driver

    # 返回首页页面对象
    def get_search_page(self):
        return Login_page(self.driver)
    def loc_page(self):
        return Home_page(self.driver)
