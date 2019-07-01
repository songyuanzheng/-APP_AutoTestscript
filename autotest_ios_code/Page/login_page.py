# -*- coding: UTF-8 -*-
from  Base.Base import Base
import Page

class Login_page(Base):
    def __init__(self, driver):
        Base.__init__(self,driver)
    def click_search_btn(self):
        # 点击我的按钮
        self.click_element(Page.wode_btn,timeout=15)
        self.click_element(Page.login_btn,timeout=15)
    def search_input_name(self, text):
        # 输入用户名
        self.input_element(Page.input_name, text,timeout=15)
    def search_input_pass(self, text):
        #输入密码
        self.input_element(Page.input_password,text,timeout=15)
    def click_bt(self):
        self.click_element(Page.login_bt,timeout=15)
