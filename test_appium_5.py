import pytest
from appium import webdriver
import logging

from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        desired_caps = {}
        # 跳过一些安装和权限的设置，可以大大提升脚本执行时间
        desired_caps["skipDeviceInitialization"] = "true"
        desired_caps["platformName"] = "Android"
        desired_caps["devicesName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["skipDeviceInitialization"] = "true"
        # 屏蔽弹窗
        desired_caps["noReset"] = "true"
        # 首次启动之后不关闭APP
        desired_caps["dontStopAppOnReset"] = "true"
        desired_caps["unicodeKeyBoard"] = "true"
        desired_caps["resetKeyBoard"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待五秒
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()
    # def test_search(self):
    #     print("这是一条搜索用例")
    #     """1.打开雪球APP
    #     2.点击收缩输入框
    #     3.像搜索输入框里面输入阿里巴巴
    #     4，在搜索结果里面选择阿里巴巴进行点击
    #     5.获取这只上 阿里巴巴 的顾家，并且顾家价格>100"""
    #     self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    #     self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
    #     self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']").click()
    #     current_price= float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
    #     assert current_price>100
    # def test_attr(self):
    #     """
    #     打开雪球应用
    #     定位首页的搜索框
    #     判断搜索框是否可用，并查看name属性
    #     打印搜索框这个元素的左上角坐标和他的宽度
    #     向搜索框输入：alibaba
    #     判断阿里巴巴是否可见
    #     如果可见打印搜索成功，不可见打印搜索失败
    #     :return:
    #     """
    #     element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    #     search_enabled = element.is_enabled()
    #     print(element.text)
    #     print(element.location)
    #     print(element.size)
    #     if search_enabled == True:
    #         element.click()
    #         self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
    #         alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']")
    #         # alibaba_element.is_displayed()
    #         # 判断元素是否可见
    #         element_display = alibaba_element.get_attribute("displayed")
    #         if element_display =="true":
    #             print("搜索成功")
    #         else:
    #             print("搜索失败")
    def test_touchaction(self):
        action = TouchAction(self.driver)
        action.press(x=344,y=1097).wait(200).move_to(x=731,y=463).release().perform()


if __name__ == '__main__':
    pytest.main()





















