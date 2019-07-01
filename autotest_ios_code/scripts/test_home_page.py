# -*- coding: UTF-8 -*-
import sys,os

import time

import pytest

sys.path.append(os.getcwd())
from Base.get_driver import get_driver
from Page.Page_p import Page
import allure


class Test_Home_Page:
    def setup_class(self):
        # 实例化base类
        self.page_obj = Page(get_driver())
    def teardown_class(self):
        # 退出driver
        self.page_obj.driver.quit()
        #确定执行顺序函数
    @pytest.mark.run(order=1)
    @allure.step("No.1--点击首页")
    def test_click_home_page(self):
        # 点击首页按钮
        self.page_obj.loc_page().click_home_page()
    @allure.step("No.2--点击定位按钮")
    def test_location_btn(self):
        #点击定位按钮
        self.page_obj.loc_page().click_location_page()
        #点击北京市
        self.page_obj.loc_page().click_location_beijing()
    @allure.step("No3.--浏览首页滚动页面——健康咨询模块")
    def test_home_page(self):
        self.page_obj.loc_page().mov_to()
        self.page_obj.loc_page().mov_to_back()
        self.page_obj.loc_page().mov_to_home()
        self.page_obj.loc_page().jie_tu()
    @allure.step("No4.--浏览首页滚动页面——健康咨询模块-子模块_育儿咨询")
    def test_home_page_baby(self):
        #点击首页健康资讯中的育儿资讯
        self.page_obj.loc_page().click_home_page_baby()

