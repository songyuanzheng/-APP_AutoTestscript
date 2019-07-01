# -*- coding: UTF-8 -*-
from  Base.Base import Base
import Page
import time
class Home_page(Base):
    def __init__(self, driver):
        Base.__init__(self,driver)
        #点击首页
    def click_home_page(self):
        self.click_element(Page.home_page_btn,timeout=15)
        #点击定位按钮
    def click_location_page(self):
        self.click_element(Page.location_page,timeout=15)
        #选择北京市
    def click_location_beijing(self):
        self.click_element(Page.location_beijing,timeout=15)
        time.sleep(3)
    def mov_to(self):
        #实现滑屏操作
        self.swipe_Up()
    def mov_to_back(self):
        # 返回定位页面返回按钮
        self.swipe_Down()
        time.sleep(3)
    def mov_to_home(self):
        #回到页面首页顶部
        self.swipe_Down()
        time.sleep(3)
    def click_home_page_baby(self):
        #点击首页育儿模块
        self.click_element(Page.baby,timeout=15)
        time.sleep(3)
    def click_home_page_baby_news(self):
        #点击育儿模块下的资讯
        self.click_element(Page.news,timeout=15)
        self.search_element(Page.i,timeout=15)
    def jie_tu_a(self):
        self.jie_tu()


