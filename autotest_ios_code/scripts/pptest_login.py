# -*- coding: UTF-8 -*-
import sys,os
sys.path.append(os.getcwd())
from Base.get_driver import get_driver
from Page.Page_p import Page
import allure
import pytest
import time
# @pytest.fixture(params=[{"input":"1","value":"休眠"},{"input":"ip","value":"IP地址"},{"input":"mtp","value":"媒体设备(MTP)"}])
# def data(request):
#     return request.param
class Test_Search:
    def setup_class(self):
        # 实例化base类
        self.page_obj = Page(get_driver())
    def teardown_class(self):
        # 退出driver
        self.page_obj.driver.quit()

    @pytest.fixture(scope="class",autouse=True)
    @allure.step("No.1--点击我的按钮")
    def test_click_wode(self):
        # 点击我的按钮
        self.page_obj.get_search_page().click_search_btn()

    @allure.step("No.2--点击登录按钮")
    def test_input_text(self):
        self.page_obj.get_search_page().search_input_name("17600769405")
        self.page_obj.get_search_page().search_input_pass("987654321")
        #点击登录按钮
        self.page_obj.get_search_page().click_bt()
        time.sleep(5)



# # 获取结果列表
        # result = (By.ID,"com.android.settings:id/title")
        # expect_list = self.base_obj.search_elements(result,15)
        # assert data.get("value") in [i.text for i in expect_list]

