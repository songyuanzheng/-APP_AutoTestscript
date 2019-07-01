# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

'''
    登录页面
'''
# 点击我的按钮
wode_btn = (By.XPATH, '//*[contains(@content-desc,"我的")]')
# 点击登录按钮
login_btn = (By.XPATH, "//*[contains(@content-desc,'登录')]")
# 点击输入按钮
input_name = (By.ID, "phone")
input_password = (By.ID, "forget")
# 点击登录按钮
login_bt = (By.XPATH, "//*[contains(@content-desc,'登录')]")

"""
首页内容
"""
#点击首页
home_page_btn = (By.XPATH, "//*[contains(@content-desc,'首页')]")
#点击定位按钮
location_page = (By.XPATH, "//*[contains(@content-desc,'sityr')]")
#点击热门城市中的北京市
location_beijing = (By.XPATH, "//*[contains(@content-desc,'北京市')]")
#实现滑动屏幕操作
loc11 = (By.XPATH, "//*[contains(@content-desc,'安阳市')]")
loc22 = (By.XPATH, "//*[contains(@content-desc,'重庆市')]")
#定位页面返回按钮
home_back = (By.XPATH, "//*[contains(@content-desc,'')]")
#点击首页健康资讯模块下育儿_子模块
baby = (By.XPATH, "//*[contains(@content-desc,'育儿')]")
#点击育儿_子模块_如何给婴儿洗头资讯
news = (By.XPATH, "//*[contains(@content-desc,'如何给婴儿洗头 教你最正确的方法')]")
i = (By.XPATH, "//*[contains(@content-desc,'资讯详情')]")




